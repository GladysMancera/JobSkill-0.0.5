from django.db import models
from paginaEmpresa.models import Puesto
from jobskill1.models import Usuarios

# Create your models here.
class Solicitud(models.Model):
    postulante=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE)
    cv = models.FileField(upload_to="Candidatos")
    solicitudD = models.CharField(max_length=100, blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)  

