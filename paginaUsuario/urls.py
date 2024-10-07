from django.urls import path
from django.conf import settings
from paginaUsuario.views import *
from django.conf.urls.static import static


urlpatterns=[
    path('perfil/', perfil, name="perfilU"),
    path('', trabajos, name="homeU"),
    path('trabajosD/', trabajosD, name="trabajosDU"),
    path('resultado/', resultado, name="resultadoU"),
    path('postulacion/', postulacion, name="postulacion"),
    path('notificacion/', notificacion, name="notificacion"),
    path('editar_perfil', editar_perfil, name='editar_perfil'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)