from django.urls import path
from paginaEmpresa.views import *

urlpatterns=[
    path('', home, name="homeE"),
    path('agregar/', agregar, name="agregar"),
    path('perfil/', perfil, name="perfil"),
    path('solicitud/', solicitud, name="solicitud"),
    path('candidato/', postulante, name="candidato"),
]
