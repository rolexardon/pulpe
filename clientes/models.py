from django.db import models

class cliente(models.Model):
	nombre = models.CharField(max_length=250,null=False)
	celular = models.CharField(max_length=8,blank=True,null=True)
	correo = models.EmailField(max_length=70, null=False, unique=True)
	
	def __unicode__(self):
		return '%s' % self.nombre
	
class saldo_cliente(models.Model):
	cliente = models.ForeignKey(cliente)
	saldo = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	
	def __unicode__(self):
		return '%s | %s' % (self.cliente.nombre,self.saldo)