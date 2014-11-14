from django.db import models
from clientes.models import cliente
from inventario.models import producto_precio,disponibilidad
from clientes.models import saldo_cliente
from decimal import *
import datetime

STATUS_CHOICES = (
    (1, 'PENDIENTE'),
    (2, 'PAGADA'),
)
PAYMENT_CHOICES = (
    (1, 'TIGOMONEY'),
    (2, 'BAC'),
	(3, 'FICOHSA'),
    (4, 'ATLANTIDA'),
	(5, 'OCCIDENTE'),
    (6, 'EFECTIVO'),
)
TIPO_DESC = (
	(1, 'PORCENTAJE'),
    (2, 'MONTO'),
)

class impuesto(models.Model):
	identificador = models.CharField(max_length=4,null=False)
	valor_decimal = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	
class descuento(models.Model):
	identificador = models.CharField(max_length=4,null=False)
	valor_decimal = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	
class factura(models.Model):
	cliente = models.ForeignKey(cliente)
	estado = models.IntegerField(choices=STATUS_CHOICES,default=1,null=False)
	metodo_pago = models.IntegerField(choices=PAYMENT_CHOICES,default=6,null=False)
	detalles = models.TextField(blank=True,null=True)
	enviada = models.BooleanField(default=False)
	
	subtotal_factura = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	otros_cargos = models.DecimalField(max_digits=6, decimal_places=2,null=True, default = 0.0)
	impuesto = models.ForeignKey(impuesto,blank=True,null=True)
	#descuento  = models.ForeignKey(descuento,blank=True,null=True)
	descuento  = models.DecimalField(max_digits=6, decimal_places=2,null=True, default = 0.0)
	saldo_utilizado = models.DecimalField(max_digits=6, decimal_places=2,null=True, default = 0.0)
	total_abonado = models.DecimalField(max_digits=6, decimal_places=2,null=True, default = 0.0)
	total_pendiente = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	
	fecha_apertura = models.DateField(auto_now_add=True, null=False)
	fecha_cierre = models.DateField(blank = True, null=True)
	
	class Meta:
		ordering = ['-fecha_apertura','cliente__nombre']
		
	def __unicode__(self):
		return '%s %s(Total: %s | Por Pagar: %s)' % (self.cliente.nombre,self.fecha_apertura,self.subtotal_factura,self.total_pendiente) 
		
	
	def save(self, *args, **kwargs):
		cl = self.cliente
		total = self.subtotal_factura + self.otros_cargos - self.descuento - self.total_abonado - self.saldo_utilizado
		
		saldo_afavor = get_saldo(cl,total)
		total = total - saldo_afavor
		saldo_afavor = self.saldo_utilizado + saldo_afavor
		self.saldo_utilizado = saldo_afavor
		self.total_pendiente = total
		
		if self.estado == 1:
			self.fecha_cierre = None
		if self.estado == 2:
			self.fecha_cierre = datetime.datetime.now()
		
		super(factura, self).save(*args, **kwargs)
	
	
class producto_factura(models.Model):
	factura = models.ForeignKey(factura)
	producto_precio = models.ForeignKey(producto_precio)
	cantidad = models.IntegerField(null=False,default=1)
	subtotal = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	
	def __unicode__(self):
		return '%s' % self.producto_precio.producto.nombre
		
	def save(self, *args, **kwargs):
		factura = self.factura
		producto_precio = self.producto_precio
		cantidad = self.cantidad
		
		subtotal_actual = factura.subtotal_factura
		
		pf = producto_factura.objects.filter(factura = factura,producto_precio=producto_precio)
		if pf:
			pf = pf[0]
			cantidad_actual = pf.cantidad
			nueva_cantidad = self.cantidad
			
			subtotal_actual = subtotal_actual - pf.subtotal
			
			
			d = disponibilidad.objects.get(producto=producto_precio.producto)
			diferencia = abs(cantidad - cantidad_actual)
			
			if cantidad_actual < cantidad:#se agregan productos
				d.cantidad = d.cantidad - diferencia
			if cantidad_actual > cantidad:#se restan
				d.cantidad = d.cantidad + diferencia
				
			d.save()
				
			"""
			d = disponibilidad.objects.filter(producto=producto_precio.producto)
			if d:
				d=d[0]
				if cantidad_actual > nueva_cantidad:
					d.cantidad = d.cantidad + (cantidad_actual - nueva_cantidad)
				else:
					d.cantidad = d.cantidad - (cantidad_actual - nueva_cantidad)
				d.save()
			"""
		else:
			d = disponibilidad.objects.filter(producto=producto_precio.producto)
			if d:
				d=d[0]
				d.cantidad = d.cantidad - cantidad
				d.save()
		
		total_producto_factura = producto_precio.precio * cantidad
		
		subtotal_actual = subtotal_actual + total_producto_factura
		self.subtotal = total_producto_factura
		
		factura.subtotal_factura = subtotal_actual
		factura.save()
		
		super(producto_factura, self).save(*args, **kwargs)
		
	def delete(self, *args, **kwargs):
		factura = self.factura
		producto_precio = self.producto_precio
		cantidad = self.cantidad
		
		d = disponibilidad.objects.filter(producto=producto_precio.producto)
		if d:
			d=d[0]
			d.cantidad = d.cantidad + cantidad
			d.save()
		
		total_actual = factura.subtotal_factura
		total_producto_factura = producto_precio.precio * cantidad
		total = Decimal(str(total_actual)) - total_producto_factura

		factura.subtotal_factura = total
		factura.save()
		
		super(producto_factura, self).delete()
	
class abono_factura(models.Model):
	factura = models.ForeignKey(factura)
	abono = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	
	fecha_cierre = models.DateField(null=False)
	

def get_saldo(cliente,total):
	try:
		scliente = saldo_cliente.objects.filter(cliente=cliente)
		if scliente:
			scliente = scliente[0]
			saldo= scliente.saldo
			if saldo > 0:
				if total <= saldo: 
					scliente.saldo = saldo-total
					scliente.save()
					return total
				else:
					scliente.saldo = 0
					scliente.save()
					return saldo
			else:
				return 0
		else:
			return 0
	except Exception,e:
		print e
		return 0
	