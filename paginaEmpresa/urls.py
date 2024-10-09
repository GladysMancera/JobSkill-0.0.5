from django.urls import path
from paginaEmpresa.views import *

urlpatterns=[
    path('', home, name="homeE"),
    path('agregar/', agregar, name="agregar"),
    path('perfil/', perfil, name="perfil"),
    path('solicitud/', solicitud, name="solicitud"),
    path('editar_perfilE/', editar_perfilE, name="editar_perfilE"),
    path('editar_agregar/',editar_agregar, name="editar_agregar")


]
