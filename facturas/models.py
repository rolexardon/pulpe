from django.db import models
from clientes.models import cliente
from inventario.models import producto_precio

STATUS_CHOICES = (
    (1, 'PENDIENTE'),
    (2, 'PAGADA'),
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
	impuesto = models.ForeignKey(impuesto)
	descuento  = models.ForeignKey(descuento)
	saldo_utilizado = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	total_factura = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	total_abonado = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	total_pendiente = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	
	fecha_apertura = models.DateField(auto_now_add=True, null=False)
	fecha_cierre = models.DateField(blank = True, null=True)
	
class producto_factura(models.Model):
	factura = models.ForeignKey(factura)
	producto_precio = models.ForeignKey(producto_precio)
	cantidad = models.IntegerField(null=False)
	subtotal = models.DecimalField(max_digits=6, decimal_places=2,null=False) 
	
class abono_factura(models.Model):
	factura = models.ForeignKey(factura)
	abono = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	
	fecha_cierre = models.DateField(null=False)
	

	