from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    link_web = models.URLField(default='')
    image = models.ImageField(upload_to='imagenes', blank=True, null=True, default="")
