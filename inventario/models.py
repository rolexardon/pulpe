from django.db import models


CATEGORIAS = (
    ('S', 'Salados'),
    ('D', 'Dulces'),
    ('R', 'Refrescos'),
    ('M', 'Medicamentos'),
	('O', 'Otros'),
)

class producto(models.Model):
	nombre = models.CharField(max_length=250,null=False)
	marca = models.CharField(max_length=150,null=False)
	imagen = models.ImageField(upload_to = 'resources/imgs/productos/',blank=True,null=True)
	detalles = models.CharField(max_length=500,null=False)
	proveedor = models.CharField(max_length=250,null=False)
	costo = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	precio = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	categoria = models.CharField(max_length=2,choices=CATEGORIAS,null=False)
	
	def __unicode__(self):
		return '%s' % (self.nombre) 
	
class disponibilidad(models.Model):
	producto = models.ForeignKey(producto, unique=True)
	cantidad = models.IntegerField(null=False)
	
	def __unicode__(self):
		return '%s' % (self.producto.nombre) 
	
class compra(models.Model):
	fecha = models.DateField(null=False)
	total_compra = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	
	def __unicode__(self):
		return '%s' % (self.fecha) 
	
class producto_compra(models.Model):
	compra = models.ForeignKey(compra)
	producto = models.ForeignKey(producto)
	cantidad = models.IntegerField(null=False)
	costo = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	
	def __unicode__(self):
		return '[%s] %s' % (self.compra.fecha, self.producto.nombre)
		
	def save(self, *args, **kwargs):
		producto = self.producto
		cantidad = self.cantidad
		
		d = disponibilidad(producto=producto,cantidad=cantidad)
		d.save()
		
		super(producto_compra, self).save(*args, **kwargs)
	
class producto_abastecimiento(models.Model):
	producto = models.ForeignKey(producto)
	minimo = models.IntegerField(null=False)
	
	def __unicode__(self):
		return '%s' % (self.producto.nombre)