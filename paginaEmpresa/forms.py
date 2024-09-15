from django import forms
from .models import Puesto

class PuestoForm(forms.ModelForm):
    class Meta:
        model=Puesto
        fields=["nombrePuesto", "descripcion", "requisitos", "sueldoBase", "beneficios", "disponibles"]
        labels = {
            'nombrePuesto': 'Nombre del Puesto',
            'descripcion': 'Descripción del Puesto',
            'requisitos': 'Requisitos para el Puesto',
            'sueldoBase': 'Sueldo Base en Pesos Mexicanos (Por Semana)',
            'beneficios': 'Beneficios Ofrecidos',
            'disponibles': 'Vacantes Disponibles'
        }