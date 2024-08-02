from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "paginaUsuario/home.html")
def perfil(request):
    return render(request, "paginaUsuario/perfil.html")