from django import forms
from .models import Contacto, ServicioB

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields='__all__'

class ServicioForm(forms.ModelForm):

    class Meta:
        model= ServicioB
        fields='__all__'
