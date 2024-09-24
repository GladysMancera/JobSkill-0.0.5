from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import solicitudForm
from paginaEmpresa.models import Puesto
from jobskill1.models import Empresa


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
@login_required
def trabajos(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    puestos=Puesto.objects.all()
    return render(request, "paginaUsuario/trabajos.html", {"puestos":puestos})
@login_required
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
@login_required
def postulacion(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    id=request.GET.get("id")
    if id is not None:
        try:
            id=int(id)
        except:
            return HttpResponseBadRequest("ID no es un número válido.")
    puesto=Puesto.objects.get(id=id)
    empresa=Empresa.objects.get(nombre=puesto.empresa)
    form=solicitudForm()
    return render(request, "paginaUsuario/postulacion.html", {"form":form, "puesto":puesto, "empresa":empresa})
def notificacion(request):
    if request.user.is_authenticated:
        if request.user.empresa==True:
            return redirect("homeE")
    return render(request, "paginaUsuario/notificacion.html")
