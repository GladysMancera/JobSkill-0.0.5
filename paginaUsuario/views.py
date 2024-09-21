from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import solicitudForm


# Create your views here.
@login_required
def home(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/home.html")
@login_required
def perfil(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/perfil.html")
def registro(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/registro.html")
def trabajos(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/trabajos.html")
def trabajosD(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/trabajosD.html")
def resultado(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/resultado.html")
def postulacion(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    form=solicitudForm()
    return render(request, "paginaUsuario/postulacion.html", {"form":form})
def notificacion(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/notificacion.html")
