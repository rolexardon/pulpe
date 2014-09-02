from django.db import models

class producto(models.Model):
	nombre = models.CharField(max_length=250,null=False)
	marca = models.CharField(max_length=150,null=False)
	detalles = models.CharField(max_length=500,null=False)
	proveedor = models.CharField(max_length=250,null=False)
	costo = models.DecimalField(max_digits=6, decimal_places=2,null=False)
	precio = models.DecimalField(max_digits=6, decimal_places=2,null=False)
    cantidad = models.IntegerField(null=False)


	