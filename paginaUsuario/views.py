from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, "paginaUsuario/home.html")
def perfil(request):
    return render(request, "paginaUsuario/perfil.html")
def registro(request):
    return render(request, "paginaUsuario/registro.html")
def trabajos(request):
    return render(request, "paginaUsuario/trabajos.html")
def trabajosD(request):
    return render(request, "paginaUsuario/trabajosD.html")
def resultado(request):
    return render(request, "paginaUsuario/resultado.html")
def postulacion(request):
    return render(request, "paginaUsuario/postulacion.html")
def notificacion(request):
    return render(request, "paginaUsuario/notificacion.html")
