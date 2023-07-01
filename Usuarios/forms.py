from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import *

class registroUsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        help_texts = {k:"" for k in fields}


class edicionUsuarioForm(UserChangeForm):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()

    class Meta():
        model = UserProfile
        fields = ['username', 'email', 'descripcion', 'link_web', 'image']
        help_texts = {k:"" for k in fields}



class changePasswordForm(PasswordChangeForm):
    new_password1 = forms.CharField(label='Nueva Contraseña', widget=forms.PasswordInput)

    class Meta():
        model = UserProfile
        fields = ['new_password']
        help_texts = {k:"" for k in fields}