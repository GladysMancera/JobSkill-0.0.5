from django.urls import path
from paginaEmpresa.views import *

urlpatterns=[
    path('', home, name="homeE"),
    path('agregar/', agregar, name="agregar"),
    path('editar/', editar, name="editar"),
     path('perfil/', perfil, name="perfil"),
]