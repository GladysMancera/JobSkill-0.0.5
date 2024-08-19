from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models.signals import post_save

class CustomUser(AbstractUser):
    empresa=models.BooleanField(default=False)
    usuario=models.BooleanField(default=False)

    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions_set", blank=True)

class Empresa(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profileE')
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=255)
    direccion=models.CharField(max_length=100)
    objetivo=models.CharField(max_length=255)
    telefono=models.CharField(max_length=16)

    def __str__(self):
        return self.nombre

class Usuarios(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profileU')
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=16)
    email=models.EmailField()
    apellido=models.CharField(max_length=50)
    apellido2=models.CharField(max_length=50, blank=True, null=True)
    genero=models.CharField(max_length=50)
    foto=models.ImageField(upload_to="Usuarios", blank=True, null=True)
    fecha_nacimiento=models.DateField()
    def __str__(self):
        return self.nombre

""" 
def crearPerfil(sender, instance, created, **kwargs):
    if created:
        Empresa.objects.create(user=instance)

def guardarPerfilEmpresa(sender, instance, **kwargs):
       instance.profileU.save()

post_save.connect(crearPerfil, sender=User)
post_save.connect(guardarPerfilEmpresa, sender=User)
"""  