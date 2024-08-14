from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "paginaEmpresa/home.html")

@login_required
def agregar(request):
    return render(request, "paginaEmpresa/agregar.html")

def editar(request):
    return render(request, "paginaEmpresa/editar.html")

def perfil(request):
    return render(request, "paginaEmpresa/perfil.html")

def solicitud(request):
    return render(request, "paginaEmpresa/solicitud.html")