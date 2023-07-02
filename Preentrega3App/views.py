from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from Preentrega3App.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.utils import timezone



def inicio(request):
    return render (request, 'inicio.html')

def contactoFormulario(request):
    if request.method == "POST":
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid(): 
            info = formulario.cleaned_data
            contacto = Contacto (nombre_contacto = info['nombre_contacto'], mail_contacto = info['mail_contacto'], asunto_contacto = info['asunto_contacto'], texto_contacto = info['texto_contacto']) 
            contacto.save()
            return render (request,'Preentrega3App/inicio.html')
    else:
        formulario = ContactoFormulario()
    return render (request, 'Preentrega3App/contacto_formulario.html', {'formulario':formulario})

class contactoList (ListView):
    model = Contacto
    template_name = "Preentrega3App/contacto_list.html"
    
class contactoDetail (DetailView):
    model = Contacto
    template_name = "Preentrega3App/contacto_detail.html"


class sobreNosotrosCreate (CreateView):
    model = SobreNosotros
    success_url = "/sobrenosotros/"
    fields = ["titulo_sobre_nosotros", "texto_sobre_nosotros"]

class sobreNosotrosList (ListView):
    model = SobreNosotros
    template_name = "Preentrega3App/sobrenosotros.html"

class sobreNosotrosUpdate (UpdateView):
    model = SobreNosotros
    success_url = "/sobrenosotros/"
    fields = ["titulo_sobre_nosotros", "texto_sobre_nosotros"]


class playasList (ListView):
    model = Playas
    template_name = "Preentrega3App/playas_list.html"

class PlayasDetail (DetailView):
    model = Playas
    template_name = "Preentrega3App/playas_detail.html"

class playasUpdate (UpdateView):
    model = Playas
    success_url = "/playaslist/"
    fields = ["nombre_playa", "descripcion_playa", "desc_abreviada_playa", "img_playa"]

    def test_func(self):
        return self.request.user.is_superuser

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['img_playa'].disabled = True
        return form

class playasCreate (CreateView):
    model = Playas
    success_url = "/playaslist/"
    fields = ["nombre_playa", "descripcion_playa", "desc_abreviada_playa", "img_playa"]

    def form_valid(self, form):
        form.instance.fecha_creado = timezone.now()
        return super().form_valid(form)
    
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user.username
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['img_playa'].disabled = True
        return form

class playasDelete (DeleteView):
    model = Playas
    success_url = "/playaslist/"

def buscar_playa(request):

    if request.GET ["nombre_playa"]:
        nombre = request.GET['nombre_playa']
        playa = Playas.objects.filter(nombre_playa__icontains = nombre).first()

        if playa:
            return redirect ("PlayasDetail", pk=playa.id)

    return render (request, 'Preentrega3App/playas_list.html', {playa: 'playa'})


class pueblosList (ListView):
    model = Pueblos
    template_name = "Preentrega3App/pueblos_list.html"

class pueblosDetail (DetailView):
    model = Pueblos
    template_name = "Preentrega3App/pueblos_detail.html"

class pueblosUpdate (UpdateView):
    model = Pueblos
    success_url = "/puebloslist/"
    fields = ["nombre_pueblo", "descripcion_pueblo", "desc_abreviada_pueblo", "img_pueblo"]

    def test_func(self):
        return self.request.user.is_superuser

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['img_pueblo'].disabled = True
        return form


class pueblosCreate (CreateView):
    model = Pueblos
    success_url = "/puebloslist/"
    fields = ["nombre_pueblo", "descripcion_pueblo", "desc_abreviada_pueblo", "img_pueblo"]

    def form_valid(self, form):
        form.instance.fecha_creado = timezone.now()
        return super().form_valid(form)
    
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user.username
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['img_pueblo'].disabled = True
        return form

class pueblosDelete (DeleteView):
    model = Pueblos
    success_url = "/puebloslist/"


def buscar_pueblo(request):

    if request.GET ["nombre_pueblo"]:
        nombre = request.GET['nombre_pueblo']
        pueblo = Pueblos.objects.filter(nombre_pueblo__icontains = nombre).first()

        if pueblo:
            return redirect ("PueblosDetail", pk=pueblo.id)

    return render (request, 'Preentrega3App/pueblos_list.html', {pueblo: 'pueblo'})


class senderismoList (ListView):
    model = Senderismo
    template_name = "Preentrega3App/senderismo_list.html"
    
class senderismoDetail (DetailView):
    model = Senderismo
    template_name = "Preentrega3App/senderismo_detail.html"

class senderismoUpdate (UpdateView):
    model = Senderismo
    success_url = "/senderismolist/"
    fields = ["nombre_ruta", "desc_abreviada_ruta", "descripcion_ruta", "dificultad", "altitud_max", "localidad_origen", "img_senderismo"]

    def test_func(self):
        return self.request.user.is_superuser

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['img_senderismo'].disabled = True
        return form


class senderismoCreate (CreateView):
    model = Senderismo
    success_url = "/senderismolist/"
    fields = ["nombre_ruta", "desc_abreviada_ruta", "descripcion_ruta", "dificultad", "altitud_max", "localidad_origen", "img_senderismo"]

    def form_valid(self, form):
        form.instance.fecha_creado = timezone.now()
        return super().form_valid(form)
    
    def form_valid(self, form):
        form.instance.usuario_creacion = self.request.user.username
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not self.request.user.is_superuser:
            form.fields['img_senderismo'].disabled = True
            
        return form

class senderismoDelete (DeleteView):
    model = Senderismo
    success_url = "/senderismolist/"


def buscar_senderismo(request):

    if request.GET ["nombre_ruta"]:
        nombre = request.GET['nombre_ruta']
        senderismo = Senderismo.objects.filter(nombre_ruta__icontains = nombre).first()

        if senderismo:
            return redirect ("SenderismoDetail", pk=senderismo.id)

    return render (request, 'Preentrega3App/senderismo_list.html', {senderismo: 'senderismo'})








