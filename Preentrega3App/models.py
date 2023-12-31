from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class SobreNosotros(models.Model):
    titulo_sobre_nosotros = models.CharField(max_length=40)
    texto_sobre_nosotros = models.CharField(max_length=700)
    fecha_creado = models.DateTimeField(default=timezone.now)
    
    class Meta:
        verbose_name_plural = "Sobre Nosotros"
    
class Playas(models.Model):
    nombre_playa = models.CharField(max_length=30)
    descripcion_playa = models.CharField(max_length=1200)
    desc_abreviada_playa = models.CharField(max_length=200)
    img_playa = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    fecha_creado = models.DateTimeField(default=timezone.now)
    usuario_creacion = models.CharField(max_length=20, default="")

    class Meta:
        verbose_name_plural = "Playas"

    def __str__(self):
        return f"{self.nombre_playa}"

class Pueblos(models.Model):
    nombre_pueblo = models.CharField(max_length=30)
    descripcion_pueblo = models.CharField(max_length=1200)
    desc_abreviada_pueblo = models.CharField(max_length=200, default="")
    img_pueblo = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    fecha_creado = models.DateTimeField(default=timezone.now)
    usuario_creacion = models.CharField(max_length=20, default="")
    
    class Meta:
        verbose_name_plural = "Pueblos"

    def __str__(self):
        return f"{self.nombre_pueblo}"

class Senderismo(models.Model):
    nombre_ruta = models.CharField(max_length=20)
    desc_abreviada_ruta = models.CharField(max_length=200, default="")
    dificultad = models.CharField(max_length=10)
    altitud_max = models.CharField(max_length=15)
    localidad_origen = models.CharField(max_length=20)
    descripcion_ruta = models.CharField(max_length=1200)
    img_senderismo = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    fecha_creado = models.DateTimeField(default=timezone.now)
    usuario_creacion = models.CharField(max_length=20, default="")


    class Meta:
        verbose_name_plural = "Senderismo"

    def __str__(self):
        return f"{self.nombre_ruta}"

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=25)
    mail_contacto = models.EmailField()
    asunto_contacto = models.CharField(max_length=30)
    texto_contacto = models.CharField(max_length=700)
    
    class Meta:
        verbose_name_plural = "Contacto"



    







