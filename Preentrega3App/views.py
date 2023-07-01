from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from Preentrega3App.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import registroUsuarioForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def inicio(request):
    return render (request, 'inicio.html')

def sobrenosotros (request):
    return render (request, 'sobrenosotros.html')

def playas(request):
    return render (request, 'playas.html')

def pueblos(request):
    return render (request, 'pueblos.html')

def senderismo(request):
    return render (request, 'senderismo.html')

def playasFormulario(request):
    if request.method == "POST":
        formulario = PlayasFormulario(request.POST)
        if formulario.is_valid(): 
            info = formulario.cleaned_data
            playa = Playas (nombre_playa = info['nombre_playa'], descripcion_playa = info['descripcion_playa'], transporte_publico = info['transporte_publico'], servicios_playa = info['servicios_playa'],terreno = info['terreno'],distancia_ciudad = info['distancia_ciudad'])
            playa.save()
            return render (request,'Preentrega3App/index.html')
    else:
        formulario = PlayasFormulario()
    return render (request, 'Preentrega3App/playas_formulario.html', {'formulario':formulario})

def pueblosFormulario(request):
    if request.method == "POST":
        formulario = PueblosFormulario(request.POST)
        if formulario.is_valid(): 
            info = formulario.cleaned_data
            pueblo = Pueblos (nombre_pueblo = info['nombre_pueblo'], descripcion_pueblo = info['descripcion_pueblo'], transporte_publico = info['transporte_publico'],distancia_ciudad_pueblo = info['distancia_ciudad_pueblo'])
            pueblo.save()
            return render (request,'Preentrega3App/index.html')
    else:
        formulario = PueblosFormulario()
    return render (request, 'Preentrega3App/pueblos_formulario.html', {'formulario':formulario})

def senderismoFormulario(request):
    if request.method == "POST":
        formulario = SenderismoFormulario(request.POST)
        if formulario.is_valid(): 
            info = formulario.cleaned_data
            senderismo = Senderismo (nombre_ruta = info['nombre_ruta'], dificultad = info['dificultad'], recorrido = info['recorrido'], localidad_origen = info['localidad_origen'], descripcion_ruta = info['descripcion_ruta']) 
            senderismo.save()
            return render (request,'Preentrega3App/index.html')
    else:
        formulario = SenderismoFormulario()
    return render (request, 'Preentrega3App/senderismo_formulario.html', {'formulario':formulario})

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

def busquedaPlaya(request):
    return render (request, "Preentrega3App/busqueda.html")

def buscar_playa(request):

    if request.GET ["nombre_playa"]:
        nombre = request.GET['nombre_playa']
        playa = Playas.objects.filter(nombre_playa__icontains = nombre).first()

        if playa:
            return redirect ("PlayasDetail", pk=playa.id)

    return render (request, 'Preentrega3App/playas_list.html', {playa: 'playa'})

def buscar_pueblo(request):

    if request.GET ["nombre_pueblo"]:
        nombre = request.GET['nombre_pueblo']
        pueblo = Pueblos.objects.filter(nombre_pueblo__icontains = nombre).first()

        if pueblo:
            return redirect ("PueblosDetail", pk=pueblo.id)

    return render (request, 'Preentrega3App/pueblos_list.html', {pueblo: 'pueblo'})

def buscar_senderismo(request):

    if request.GET ["nombre_ruta"]:
        nombre = request.GET['nombre_ruta']
        senderismo = Senderismo.objects.filter(nombre_ruta__icontains = nombre).first()

        if senderismo:
            return redirect ("SenderismoDetail", pk=senderismo.id)

    return render (request, 'Preentrega3App/senderismo_list.html', {senderismo: 'senderismo'})

class playasList (ListView):
    model = Playas
    template_name = "Preentrega3App/playas_list.html"

class PlayasDetail (DetailView):
    model = Playas
    template_name = "Preentrega3App/playas_detail.html"

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

class pueblosDelete (LoginRequiredMixin,DeleteView):
    model = Pueblos
    success_url = "/puebloslist/"




class senderismoList (ListView):
    model = Senderismo
    template_name = "Preentrega3App/senderismo_list.html"
    
class senderismoDetail (DetailView):
    model = Senderismo
    template_name = "Preentrega3App/senderismo_detail.html"

class senderismoUpdate (LoginRequiredMixin,UpdateView):
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

class senderismoDelete (LoginRequiredMixin,DeleteView):
    model = Senderismo
    success_url = "/senderismolist/"



class contactoList (ListView):
    model = Contacto
    template_name = "Preentrega3App/contacto_list.html"
    
class contactoDetail (DetailView):
    model = Contacto
    template_name = "Preentrega3App/contacto_detail.html"



class sobreNosotrosList (ListView):
    model = SobreNosotros
    template_name = "Preentrega3App/sobrenosotros.html"

class sobreNosotrosUpdate (UpdateView):
    model = SobreNosotros
    success_url = "/sobrenosotros/"
    fields = ["titulo_sobre_nosotros", "texto_sobre_nosotros"]
    

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

def login_request (request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=user, password=contraseña)

            if user is not None:
                login(request, user)

                return render(request, 'Preentrega3App/inicio.html', {'mensaje': f'Bienvenido {user}'})
            
            else:
                messages.error(request, 'Datos incorrectos')
            
        else:
            messages.error(request, 'Datos incorrectos')
        
    form = AuthenticationForm()

    return render (request, 'Preentrega3App/login.html', {'form': form})


def registro(request):
        
    if request.method == 'POST':
        form = registroUsuarioForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            usuario = form.save()

            profile = UserProfile.objects.create(user=usuario, descripcion='', link_web='', image='')
            return render(request, 'Preentrega3App/inicio.html', {"mensaje":"Se ha registrado con éxito"})
            
    else:
        form = registroUsuarioForm()

    return render (request, 'Preentrega3App/registro.html', {'form': form})

class Logout(LogoutView):
    template_name= 'Preentrega3App/logout.html'


def editarPerfil(request):
    
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = edicionUsuarioForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('/inicio/')
    else:
        initial_data = {'email': user.email,'username': user.username,}
        form = edicionUsuarioForm(instance=profile, initial=initial_data)

    return render(request, 'Preentrega3App/editar_usuario.html', {'form': form, 'usuario': user})


def detalle_usuario(request):

    try:
        profile = UserProfile.objects.get(user=request.user.id)

    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    return render (request, 'user_profile_detail.html', {'profile': profile})


