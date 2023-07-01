
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    
    path('', include('Preentrega3App.urls')),
    path('admin/', admin.site.urls),
    path('Preentrega3App/', include('Preentrega3App.urls')),
    path('Usuarios/', include('Usuarios.urls')),

]
