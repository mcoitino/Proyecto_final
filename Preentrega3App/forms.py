from django import forms

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
    transporte_publico = forms.CharField(max_length=15)
    distancia_ciudad_pueblo = forms.CharField(max_length=10)

class SenderismoFormulario(forms.Form):
    nombre_ruta = forms.CharField(max_length=20)
    dificultad = forms.CharField(max_length=10)
    recorrido = forms.CharField(max_length=15)
    altitud_máxima = forms.CharField(max_length=15)
    localidad_origen = forms.CharField(max_length=20)
    descripcion_ruta = forms.CharField(max_length=700)

class ContactoFormulario(forms.Form):
    nombre_contacto = forms.CharField(max_length=25)
    mail_contacto = forms.EmailField()
    asunto_contacto = forms.CharField(max_length=30)
    texto_contacto = forms.CharField(max_length=700)