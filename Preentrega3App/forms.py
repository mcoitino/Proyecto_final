from django import forms
from .models import *


class ContactoFormulario(forms.Form):
    nombre_contacto = forms.CharField(label='Nombre', max_length=25)
    mail_contacto = forms.EmailField(label='Email',)
    asunto_contacto = forms.CharField(label='Asunto', max_length=30)
    texto_contacto = forms.CharField(label='Mensaje', max_length=700)




