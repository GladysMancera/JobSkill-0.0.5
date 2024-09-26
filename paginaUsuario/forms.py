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
        widgets = {
            'solicitudD': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Explica tus razones...'}),
            'cv': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }