from django.db import models

class Empresa(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=10)
    email=models.EmailField()

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=10)
    email=models.EmailField()
    apellido=models.CharField(max_length=50)
    genero=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()