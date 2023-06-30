from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

class PlayasFormulario(forms.Form):
    nombre_playa = forms.CharField(max_length=30)
    descripcion_playa = forms.CharField(max_length=600)
    transporte_publico = forms.CharField(max_length=15)
    servicios_playa = forms.CharField(max_length=15)
    terreno = forms.CharField(max_length=10)
    distancia_ciudad = forms.CharField(max_length=10)

class PueblosFormulario(forms.Form):
    nombre_pueblo = forms.CharField(max_length=30)
    descripcion_pueblo = forms.CharField(max_length=600)

class SenderismoFormulario(forms.Form):
    nombre_ruta = forms.CharField(max_length=20)
    dificultad = forms.CharField(max_length=10)
    recorrido = forms.CharField(max_length=15)
    altitud_máxima = forms.CharField(max_length=15)
    localidad_origen = forms.CharField(max_length=20)
    descripcion_ruta = forms.CharField(max_length=700)



class ContactoFormulario(forms.Form):
    nombre_contacto = forms.CharField(label='Nombre', max_length=25)
    mail_contacto = forms.EmailField(label='Email',)
    asunto_contacto = forms.CharField(label='Asunto', max_length=30)
    texto_contacto = forms.CharField(label='Mensaje', max_length=700)

class registroUsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        help_texts = {k:"" for k in fields}


"""class edicionUsuarioForm (UserChangeForm):
    descripcion = forms.CharField(label="Descripción", max_length=200)
    link_web = forms.URLField(label="Link a página web")
    image = forms.ImageField(label="Imagen", required=False)


    class Meta():
        model = UserProfile
        fields = ['descripcion', 'link_web', 'image','username', 'email']
        help_texts = {k:"" for k in fields}
"""

class edicionUsuarioForm(UserChangeForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta():
        model = UserProfile
        fields = ['username', 'email', 'descripcion', 'link_web', 'image']
        help_texts = {k:"" for k in fields}


