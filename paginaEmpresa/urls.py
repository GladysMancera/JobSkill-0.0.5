from django.urls import path
from paginaEmpresa.views import *

urlpatterns=[
    path('', home, name="homeE"),
]