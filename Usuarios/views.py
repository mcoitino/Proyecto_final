from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import registroUsuarioForm
from django.contrib.auth.views import LogoutView
from .models import *
from django.contrib import messages
from Usuarios.forms import *
from django.shortcuts import redirect



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

    return render (request, 'login.html', {'form': form})


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

    return render (request, 'registro.html', {'form': form})

class Logout(LogoutView):
    template_name= 'logout.html'


def editarPerfil(request):
    
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = edicionUsuarioForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            form.save()
            return redirect('/inicio/')
    else:
        initial_data = {'email': user.email,'username': user.username,}
        form = edicionUsuarioForm(instance=profile, initial=initial_data)

    return render(request, 'editar_usuario.html', {'form': form, 'usuario': user})


def detalle_usuario(request):

    try:
        profile = UserProfile.objects.get(user=request.user.id)

    except UserProfile.DoesNotExist:
        profile= None

    return render (request, 'user_profile_detail.html', {'profile': profile})


def changePassword(request):
    usuario = User.objects.get(id=request.user.id)

    if request.method == 'POST':
        form = changePasswordForm(usuario, request.POST)
        if form.is_valid():
            new_password1 = form.cleaned_data['new_password1']
            usuario.set_password(new_password1)
            usuario.save()
            return redirect('/inicio/')
    
    else:
        form = changePasswordForm(usuario)

    return render (request, 'cambio_password.html', {'form':form})