from django.db import models

class Empresa(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=255)
    direccion=models.CharField(max_length=100)
    objetivo=models.CharField(max_length=255)
    telefono=models.CharField(max_length=16)
    email=models.EmailField()

    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=16)
    email=models.EmailField()
    apellido=models.CharField(max_length=50)
    apellido2=models.CharField(max_length=50, blank=True, null=True)
    genero=models.CharField(max_length=50)
    foto=models.ImageField(upload_to="Usuarios")
    fecha_nacimiento=models.DateField()