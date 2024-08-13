from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render

# Create your views here.
#son las vistas que se han generado de la pagina 

def home(request):

    return render(request, "Jobskill1/home.html" )

def contenido(request):

     return render(request, "Jobskill1/contenido.html" )

def login(request):

     return render(request, "Jobskill1/login.html" )

def registro(request): #esta vista permite la funcion de elegir el tipo de usuario
     if request.method == 'POST':
          tipo = request.POST.get('tipo_usuario')
          if tipo == 'aspirante':
               return redirect('registroU')
          elif tipo == 'empresa':
               return redirect('registroE')
          return render(request, 'registro.html')

     return render(request, "Jobskill1/registro.html" )


def registroU(request):

     return render(request, "Jobskill1/registroU.html" )
def registroE(request):

     return render(request, "Jobskill1/RegistroE.html" )

