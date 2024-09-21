from django import forms
from .models import Solicitud

class solicitudForm(forms.ModelForm):
    class Meta:
        model=Solicitud
        fields=["solicitudD", "cv"]
        labels={
            "solicitudD":"¿Por qué deberías tener este puesto?",
            "cv":"Suba aquí su Currículum Vitae",
        }