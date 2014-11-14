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
	
	class Meta:
		ordering = ['nombre']

class proveedor(models.Model):
	nombre = models.CharField(max_length=250,null=False)
	direccion = models.CharField(max_length=500,null=False)
	
	def __unicode__(self):
		return '%s' % (self.nombre) 
		
	class Meta:
		ordering = ['nombre']
	
class producto_costo(models.Model):
	producto = models.ForeignKey(producto)
	proveedor = models.ForeignKey(proveedor)
	costo = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	activo = models.BooleanField(null=False,default=True)
	fecha_ingreso = models.DateField(null=False)
	fecha_debaja = models.DateField(blank = True,null=True)
	
	class Meta:
		unique_together = ('producto', 'proveedor','costo',)
		ordering = ['activo','producto__nombre','-fecha_ingreso']
		
	def __unicode__(self):
		return '%s | %s (%s) [Activo: %s]' % (self.producto.nombre, self.costo,self.proveedor.nombre,self.activo) 
	
class producto_precio(models.Model):
	producto = models.ForeignKey(producto)
	precio = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	activo = models.BooleanField(null=False,default=True)
	fecha_ingreso = models.DateField(null=False)
	fecha_debaja = models.DateField(blank = True,null=True)
	
	class Meta:
		unique_together = ('producto', 'precio',)
		ordering = ['activo','producto__nombre','-fecha_ingreso']
	
	def __unicode__(self):
		return '%s | %s [Activo: %s] ' % (self.producto.nombre, self.precio,self.activo) 
		
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
		
	
	def delete(self, *args, **kwargs):
		compra = self.compra
		producto_costo = self.producto_costo
		cantidad = self.cantidad
		
		total_actual = compra.total_compra
		
		d = disponibilidad.objects.filter(producto=producto_costo.producto)
		if d:
			d=d[0]
			d.cantidad = d.cantidad - cantidad
	
		total_producto_compra = producto_costo.costo * cantidad
		total = Decimal(str(total_actual)) - total_producto_compra
		
		d.save()
		compra.total_compra = total
		compra.save()
		
		super(producto_compra, self).delete(*args, **kwargs)

		
	def save(self, *args, **kwargs):
		compra = self.compra
		producto_costo = self.producto_costo
		cantidad = self.cantidad
		
		total_actual = compra.total_compra
		
		pc = producto_compra.objects.filter(compra=compra,producto_costo = producto_costo)
		if pc:
			pc=pc[0]
			d = disponibilidad.objects.get(producto=pc.producto_costo.producto)
			cantidad_actual = pc.cantidad
			diferencia = abs(cantidad - cantidad_actual)
			
			total_producto_compra = pc.producto_costo.costo * diferencia
			
			if cantidad_actual < cantidad:#se agregan productos
				d.cantidad = d.cantidad + diferencia
				total = Decimal(str(total_actual)) + total_producto_compra
			if cantidad_actual > cantidad:#se restan
				d.cantidad = d.cantidad - diferencia
				total = Decimal(str(total_actual)) - total_producto_compra

		else:
			d = disponibilidad.objects.filter(producto=producto_costo.producto)
			if d:
				d=d[0]
				d.cantidad = d.cantidad + cantidad
			else:
				d= disponibilidad(producto=producto_costo.producto,cantidad=cantidad)
			
			total_producto_compra = producto_costo.costo * cantidad
			total = Decimal(str(total_actual)) + total_producto_compra
			
		d.save()
		compra.total_compra = total
		compra.save()
		
		super(producto_compra, self).save(*args, **kwargs)
	
class producto_abastecimiento(models.Model):
	producto = models.ForeignKey(producto)
	minimo = models.IntegerField(null=False)
	
	def __unicode__(self):
		return '%s' % (self.producto.nombre)
		

	