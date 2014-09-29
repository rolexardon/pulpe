from django.db import models
from decimal import *
import os

CATEGORIAS = (
    ('S', 'Salados'),
    ('D', 'Dulces'),
    ('R', 'Bebidas'),
	('C', 'Congelados'),
    ('M', 'Medicamentos'),
	('O', 'Otros'),
)

class producto(models.Model):
	nombre = models.CharField(max_length=250,null=False)
	marca = models.CharField(max_length=150,null=False)
	imagen = models.ImageField(upload_to = 'pulpe/resources/imgs/productos/',blank=True,null=True)
	detalles = models.CharField(max_length=500,null=False)
	categoria = models.CharField(max_length=2,choices=CATEGORIAS,null=False)
	
	def __unicode__(self):
		return '%s' % (self.nombre) 

class proveedor(models.Model):
	nombre = models.CharField(max_length=250,null=False)
	direccion = models.CharField(max_length=500,null=False)
	
	def __unicode__(self):
		return '%s' % (self.nombre) 
	
class producto_costo(models.Model):
	producto = models.ForeignKey(producto)
	proveedor = models.ForeignKey(proveedor)
	costo = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	activo = models.BooleanField(null=False,default=True)
	fecha_ingreso = models.DateField(null=False)
	fecha_debaja = models.DateField(blank = True,null=True)
	
	class Meta:
		unique_together = ('producto', 'proveedor','costo',)
		
	def __unicode__(self):
		return '[%s] %s | %s (%s)' % (self.activo, self.producto.nombre, self.costo,self.proveedor.nombre) 
	
class producto_precio(models.Model):
	producto = models.ForeignKey(producto)
	precio = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	activo = models.BooleanField(null=False,default=True)
	fecha_ingreso = models.DateField(null=False)
	fecha_debaja = models.DateField(blank = True,null=True)
	
	class Meta:
		unique_together = ('producto', 'precio',)
	
	def __unicode__(self):
		return '[Activo: %s] %s | %s' % (self.activo, self.producto.nombre, self.precio) 
		
class disponibilidad(models.Model):
	producto = models.ForeignKey(producto, unique=True)
	cantidad = models.IntegerField(null=False)
	
	def __unicode__(self):
		return '%s(%s)' % (self.producto.nombre,self.cantidad) 
	
class compra(models.Model):
	fecha = models.DateField(null=False)
	total_compra = models.DecimalField(max_digits=6, decimal_places=2,null=False, default = 0.0)
	detalles = models.TextField(blank=True,null=True)
	imagen = models.ImageField(upload_to = 'pulpe/resources/imgs/compras/',blank=True,null=True)
	
	def __unicode__(self):
		return '%s(%s)' % (self.fecha,self.total_compra) 
	
class producto_compra(models.Model):
	compra = models.ForeignKey(compra)
	producto_costo = models.ForeignKey(producto_costo)
	cantidad = models.IntegerField(null=False)
	
	def __unicode__(self):
		return '[%s] %s' % (self.compra.fecha, self.producto_costo.producto.nombre)
		
	'''
	def delete(self, *args, **kwargs):
		d = disponibilidad.objects.filter(producto=producto_costo.producto)
		if d:
			d=d[0]
			d.cantidad = d.cantidad - cantidad

        super(producto_compra, self).delete(*args, **kwargs)
	'''

		
	def save(self, *args, **kwargs):
		compra = self.compra
		producto_costo = self.producto_costo
		cantidad = self.cantidad
		
		d = disponibilidad.objects.filter(producto=producto_costo.producto)
		if d:
			d=d[0]
			d.cantidad = d.cantidad + cantidad
		else:
			d= disponibilidad(producto=producto_costo.producto,cantidad=cantidad)
		d.save()
		
		total_actual = compra.total_compra
		total_producto_compra = producto_costo.costo * cantidad
		total = Decimal(str(total_actual)) + total_producto_compra
		
		compra.total_compra = total
		compra.save()
		
		super(producto_compra, self).save(*args, **kwargs)
	
class producto_abastecimiento(models.Model):
	producto = models.ForeignKey(producto)
	minimo = models.IntegerField(null=False)
	
	def __unicode__(self):
		return '%s' % (self.producto.nombre)
		

	