from django import forms
from .models import Donacion, Ayuda

class DonacionForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['cantidad', 'comentario']


class AyudaForm(forms.ModelForm):
    class Meta:
        model = Ayuda
        fields = ['tipo', 'descripcion', 'cantidad']
