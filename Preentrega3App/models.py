from django.db import models

# Create your models here.

class SobreNosotros(models.Model):
    titulo_sobre_nosotros = models.CharField(max_length=40)
    texto_sobre_nosotros = models.CharField(max_length=700)
    class Meta:
        verbose_name_plural = "Sobre Nosotros"
    
class Playas(models.Model):
    nombre_playa = models.CharField(max_length=30)
    descripcion_playa = models.CharField(max_length=600)
    transporte_publico = models.CharField(max_length=15)
    servicios_playa = models.CharField(max_length=15)
    terreno = models.CharField(max_length=10)
    distancia_ciudad = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = "Playas"

class Pueblos(models.Model):
    nombre_pueblo = models.CharField(max_length=30)
    descripcion_pueblo = models.CharField(max_length=600)
    transporte_publico = models.CharField(max_length=15)
    distancia_ciudad_pueblo = models.CharField(max_length=15)
    
    class Meta:
        verbose_name_plural = "Pueblos"

class Senderismo(models.Model):
    nombre_ruta = models.CharField(max_length=20)
    dificultad = models.CharField(max_length=10)
    recorrido = models.CharField(max_length=15)
    altitud_max = models.CharField(max_length=15)
    localidad_origen = models.CharField(max_length=20)
    descripcion_ruta = models.CharField(max_length=700)

    class Meta:
        verbose_name_plural = "Senderismo"

class Contacto(models.Model):
    nombre_contacto = models.CharField(max_length=25)
    mail_contacto = models.EmailField()
    asunto_contacto = models.CharField(max_length=30)
    texto_contacto = models.CharField(max_length=700)
    
    class Meta:
        verbose_name_plural = "Contacto"

class Presentacion(models.Model):
    titulo = models.CharField(max_length=20)
    texto = models.CharField(max_length=700)