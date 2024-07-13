from django.urls import path
from paginaUsuario.views import *

urlpatterns=[
    path('', home, name="homeU"),
]