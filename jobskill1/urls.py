from django.urls import path 

from jobskill1.views import *

#este archivo contiene las url de las vistas creadas

urlpatterns = [
    path('', home, name="home"),
    path('contenido/', contenido, name="contenido"),
    path('login/', logueo, name="login"),
    path('registro/', registro, name="registro"),
    path('logout/', cerrar, name="cerrarS"),
]