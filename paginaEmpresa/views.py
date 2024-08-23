from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, "paginaEmpresa/home.html")

@login_required
def agregar(request):
    return render(request, "paginaEmpresa/agregar.html")
@login_required
def editar(request):
    return render(request, "paginaEmpresa/editar.html")
@login_required
def perfil(request):
    return render(request, "paginaEmpresa/perfil.html")
@login_required
def solicitud(request):
    return render(request, "paginaEmpresa/solicitud.html")