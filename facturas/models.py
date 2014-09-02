from django.db import models
from cliente import clientes
from inventario import producto

STATUS_CHOICES = (
    (1, 'PENDIENTE'),
    (2, 'PAGADA'),
)

class factura(models.Model):
	cliente = models.ForeignKey(clientes)
	estado = models.IntegerField(choices=STATUS_CHOICES,default=1,null=False)
	fecha_apertura = models.DateField(auto_now_add=True, null=False)
	fecha_cierra = models.DateField(blank = True, null=True)
	
class producto_factura(models.Model):
	factura = models.ForeignKey(factura)
	producto = models.ForeignKey(producto)
	precio_actual = models.DecimalField(max_digits=6, decimal_places=2,null=False) 
	cantidad = models.IntegerField(null=False)
	subtotal = models.DecimalField(max_digits=6, decimal_places=2,null=False) 