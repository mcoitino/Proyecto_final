"""Preentrega_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Preentrega3App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', views.inicio, name = "Inicio"),
    path('sobrenosotros/', views.sobreNosotrosList.as_view(), name= "Sobre Nosotros"),
    path('playas/', views.playas, name = 'Playas'),
    path('pueblos/', views.pueblos, name = 'Pueblos'),
    path('senderismo/', views.senderismo, name = 'Senderismo'),
    path('playasformulario/', views.playasFormulario, name = 'Playas Formulario'),
    path('pueblosformulario/', views.pueblosFormulario, name = 'Pueblos Formulario'),
    path('senderismoformulario/', views.senderismoFormulario, name = 'Senderismo Formulario'),
    path('contactoformulario/', views.contactoFormulario, name = 'Contacto Formulario'),
    path('busqueda/', views.busquedaPlaya, name = 'Busqueda Playa'),
    path('buscarplaya/', views.buscar_playa, name = 'Buscar'),
    path('buscarpueblos/', views.buscar_pueblo, name = 'BuscarPueblo'),
    path('buscar-ruta/', views.buscar_senderismo, name = 'BuscarRuta'),
    path('senderismolist/', views.senderismoList.as_view(), name = 'SenderismoList'),
    path('sobrenosotros/editar/<int:pk>/', views.sobreNosotrosUpdate.as_view(), name='SobreNosotrosEditar'),
    path('crearsobrenosotros', views.sobreNosotrosCreate.as_view(), name='SobreNosotrosCrear'),
    

    path('playaslist/', views.playasList.as_view(), name = 'PlayasList'),
    path('playasdetail/editar/<int:pk>/', views.playasUpdate.as_view(), name='PlayasEditar'),
    path('crearplaya/', views.playasCreate.as_view(), name='PlayasCrear'),
    path('playasdetail/borrar/<int:pk>/', views.playasDelete.as_view(), name='PlayasBorrar'),
    path('playasdetail/<pk>/', views.PlayasDetail.as_view(), name = 'PlayasDetail'),


    path('puebloslist/', views.pueblosList.as_view(), name = 'PueblosList'),
    path('pueblosdetail/<pk>/', views.pueblosDetail.as_view(), name = 'PueblosDetail'),
    path('pueblosdetail/editar/<int:pk>/', views.pueblosUpdate.as_view(), name='PueblosEditar'),
    path('crearpueblo/', views.pueblosCreate.as_view(), name='PueblosCrear'),
    path('pueblosdetail/borrar/<int:pk>/', views.pueblosDelete.as_view(), name='PueblosBorrar'),

    path('senderismolist/', views.senderismoList.as_view(), name = 'SenderismoList'),
    path('senderismodetail/<pk>/', views.senderismoDetail.as_view(), name = 'SenderismoDetail'),
    path('senderismodetail/editar/<int:pk>/', views.senderismoUpdate.as_view(), name='SenderismoEditar'),
    path('crearsenderismo/', views.senderismoCreate.as_view(), name='SenderismoCrear'),
    path('senderismodetail/borrar/<int:pk>/', views.senderismoDelete.as_view(), name='SenderismoBorrar'),

    path('contactolist/', views.contactoList.as_view(), name = 'ContactoList'),
    path('contactodetail/<pk>/', views.contactoDetail.as_view(), name = 'ContactoDetail'),


    path('login/', views.login_request, name = "Login"),
    path('registro/', views.registro, name = "Registro"),
    path('logout/', views.Logout.as_view(), name = "Logout"),
    path('editarperfil/', views.editarPerfil, name = "EditarPerfil"),
    path('verperfil/', views.detalle_usuario, name='VerPerfil'),
    path('cambiopassword/', views.changePassword, name='CambiarPassword'),
   

]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)