from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render
from .forms import crearUsuario, crearUsuarioE

# Create your views here.
#son las vistas que se han generado de la pagina 

def home(request):

    return render(request, "Jobskill1/home.html" )

def contenido(request):

     return render(request, "Jobskill1/contenido.html" )

def login(request):

     return render(request, "registration/login.html" )

def tipoUsuario(request): #esta vista permite la funcion de elegir el tipo de usuario #No en funcionamiento
     if request.method == 'POST':
          tipo = request.POST.get('tipo_usuario')
          if tipo == 'aspirante':
               return redirect('registroU')
          elif tipo == 'empresa':
               return redirect('registroE.html')
          return render(request, 'registro.html')

     return render(request, "Jobskill1/TipoUsuario.html" )

def registroU(request): #No en funcionamiento
     crearE=crearUsuario()
     if request.method=="POST":
          formCrear=crearUsuario(data=request.POST)
          if formCrear.is_valid():
               formCrear.save()
               return render(request, "jobskill1/home.html")
          else:
               return HttpResponse('Error xd')
     return render(request, "registration/register.html", {"form" : crearE})

def registro(request):
     if request.method=="POST":
          tipo=request.session.get("tipo_usuario")
          if tipo=="1":
               formCrear=crearUsuario(data=request.POST)
               if formCrear.is_valid():
                    formCrear.save()
                    return render(request, "jobskill1/home.html")
               else:
                    return HttpResponse('Error xd')
          else:
               formCrear=crearUsuarioE(data=request.POST)
               if formCrear.is_valid():
                    formCrear.save()
                    return render(request, "jobskill1/home.html")
               else:
                    return HttpResponse('Error xd')
     else: 
          try:
               tipo=request.GET.get("tipo_usuario")
          except:
               return render(request, "jobskill1/TipoUsuario.html")
          request.session["tipo_usuario"]=tipo
          if tipo=="0":
               return render(request, "jobskill1/TipoUsuario.html")
          elif tipo=="1":
               crear=crearUsuario()
               return render(request, "registration/register.html", {"form":crear})
          elif tipo=="2":
               crear=crearUsuarioE()
               return render(request, "registration/register.html", {"form":crear})
     return render(request, "jobskill1/TipoUsuario.html")

def registroE(request): #No en funcionamiento
     return render(request, "Jobskill1/RegistroE.html" )

