from django.db import models
from clientes.models import cliente
from inventario.models import producto_precio,disponibilidad
from decimal import *

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
	impuesto = models.ForeignKey(impuesto,blank=True,null=True)
	descuento  = models.ForeignKey(descuento,blank=True,null=True)
	saldo_utilizado = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	total_factura = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	total_abonado = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	total_pendiente = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	
	fecha_apertura = models.DateField(auto_now_add=True, null=False)
	fecha_cierre = models.DateField(blank = True, null=True)
	
	def __unicode__(self):
		return '%s %s(%s)' % (self.cliente.nombre,self.fecha_apertura,self.total_factura) 
	
class producto_factura(models.Model):
	factura = models.ForeignKey(factura)
	producto_precio = models.ForeignKey(producto_precio)
	cantidad = models.IntegerField(null=False)
	subtotal = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	
	def __unicode__(self):
		return '%s' % self.producto_precio.producto.nombre
		
	def save(self, *args, **kwargs):
		factura = self.factura
		producto_precio = self.producto_precio
		cantidad = self.cantidad
		
		d = disponibilidad.objects.filter(producto=producto_precio.producto)
		if d:
			d=d[0]
			d.cantidad = d.cantidad - cantidad
		d.save()
		
		total_actual = factura.total_factura
		total_producto_factura = producto_precio.precio * cantidad
		total = Decimal(str(total_actual)) + total_producto_factura - factura.total_abonado
		
		self.subtotal = total_producto_factura
		factura.total_factura = total
		factura.total_pendiente = total
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
		
		total_actual = factura.total_factura
		total_producto_factura = producto_precio.precio * cantidad
		total = Decimal(str(total_actual)) - total_producto_factura

		factura.total_factura = total
		factura.total_pendiente = total
		factura.save()
		
		super(producto_factura, self).delete()
	
class abono_factura(models.Model):
	factura = models.ForeignKey(factura)
	abono = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	
	fecha_cierre = models.DateField(null=False)
	

	