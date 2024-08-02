from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "paginaEmpresa/home.html")

def agregar(request):
    return render(request, "paginaEmpresa/agregar.html")

def editar(request):
    return render(request, "paginaEmpresa/editar.html")

def perfil(request):
    return render(request, "paginaEmpresa/perfil.html")