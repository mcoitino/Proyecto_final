from django.shortcuts import render
from django.http import HttpResponse
from .models import Playas
from .models import Pueblos
from .models import Senderismo
from .models import Contacto
from Preentrega3App.forms import PlayasFormulario
from Preentrega3App.forms import PueblosFormulario
from Preentrega3App.forms import SenderismoFormulario
from Preentrega3App.forms import ContactoFormulario

# Create your views here.

def inicio(request):
    return render (request, 'index.html')

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
            return render (request,'Preentrega3App/index.html')
    else:
        formulario = ContactoFormulario()
    return render (request, 'Preentrega3App/contacto_formulario.html', {'formulario':formulario})

def busquedaPlaya(request):
    return render (request, "Preentrega3App/busqueda.html")

def buscar(request):
    
    #respuesta = f"buscando {request.GET ['nombre_playa']}"

    if request.GET ["nombre_playa"]:
        nombre = request.GET['nombre_playa']
        playas = Playas.objects.filter(nombre_playa__icontains = nombre)

        return render (request, 'Preentrega3App/resultadobusqueda.html', {"playas" : playas, "nombre_playa": nombre})
    
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)
