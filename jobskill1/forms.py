from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class crearUsuarioE(UserCreationForm):
    nombre_empresa=forms.CharField(max_length=50)
    descripcion=forms.CharField(max_length=255, widget=forms.Textarea())
    direccion=forms.CharField(max_length=100)
    objetivo=forms.CharField(max_length=255, widget=forms.Textarea())
    telefono=forms.CharField(max_length=16)
    foto=forms.ImageField(label="Logo")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.empresa = True
        if commit:
            user.save()
            Empresa.objects.create(
                user=user,
                nombre=self.cleaned_data.get('nombre_empresa'),
                direccion=self.cleaned_data.get('direccion'),
                telefono=self.cleaned_data.get('telefono'),
                descripcion=self.cleaned_data.get('descripcion'),
                foto=self.cleaned_data.get('foto'),
                objetivo=self.cleaned_data.get('objetivo'),
            )
        return user
    
class crearUsuario(UserCreationForm):
    nombre=forms.CharField(max_length=50)
    direccion=forms.CharField(max_length=100)
    telefono=forms.CharField(max_length=16)
    #email=forms.EmailField()
    apellido_paterno=forms.CharField(max_length=50)
    apellido_materno=forms.CharField(max_length=50, required=False)
    genero = forms.ChoiceField(choices=[('M', 'Masculino'), ('F', 'Femenino')], label="Género")
    foto=forms.ImageField()
    fecha_de_nacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Fecha de Nacimiento")

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.usuario = True
        if commit:
            user.save()
            Usuarios.objects.create(
                user=user,
                nombre=self.cleaned_data.get('nombre'),
                direccion=self.cleaned_data.get('direccion'),
                telefono=self.cleaned_data.get('telefono'),
                apellido=self.cleaned_data.get('apellido_paterno'),
                apellido2=self.cleaned_data.get('apellido_materno'),
                genero=self.cleaned_data.get('genero'),
                foto=self.cleaned_data.get('foto'),
                fecha_nacimiento=self.cleaned_data.get('fecha_de_nacimiento'),
            )
        return user