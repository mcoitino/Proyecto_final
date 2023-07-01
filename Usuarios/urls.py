
from django.contrib import admin
from django.urls import path
from Usuarios import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('login/', views.login_request, name = "Login"),
    path('registro/', views.registro, name = "Registro"),
    path('logout/', views.Logout.as_view(), name = "Logout"),
    path('editarperfil/', views.editarPerfil, name = "EditarPerfil"),
    path('verperfil/', views.detalle_usuario, name='VerPerfil'),
    path('cambiopassword/', views.changePassword, name='CambiarPassword'),

    ]