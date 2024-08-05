from django.shortcuts import render

# Create your views here.

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
