from django.db import models

class cliente(models.Model):
	nombre = models.CharField(max_length=250,null=False)
	apellido = models.CharField(max_length=250,null=False)
	cargo = models.CharField(max_length=150,null=False)
	celular = models.CharField(max_length=8,null=False)
	correo = models.EmailField(max_length=70, null=False, unique=True)