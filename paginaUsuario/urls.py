from django.urls import path
from paginaUsuario.views import *

urlpatterns=[
    path('', home, name="homeU"),
    path('perfil/', perfil, name="perfilU"),
    path('registro/', registro, name="registroU"),
    path('trabajos/', trabajos, name="trabajosU"),
    path('trabajosD/', trabajosD, name="trabajosDU"),
    path('resultado/', resultado, name="resultadoU"),

]