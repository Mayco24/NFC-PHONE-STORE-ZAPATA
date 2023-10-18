from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login
from accounts.forms import NuestroFormularioDeRegistro, NuestroEditarPerfilFormulario, NuestroFormularioCambioPassword, CustomAuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



def login(request):

    if request.method == 'POST':
        formulario = CustomAuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')

            usuario = authenticate(username=username, password=password)

            django_login(request, usuario) 

            return redirect('inicio')
    else:
        formulario = CustomAuthenticationForm()
    
    return render(request, 'accounts/login.html', {'formulario': formulario})

def registro(request):
    
    if request.method == 'POST':
        formulario = NuestroFormularioDeRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = NuestroFormularioDeRegistro()
        
    return render(request, 'accounts/registro.html', {'formulario': formulario})
        

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario = NuestroEditarPerfilFormulario(request.POST, instance= request.user)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    formulario = NuestroEditarPerfilFormulario(instance= request.user)
    return render(request, 'accounts/editar_perfil.html', {'formulario': formulario})

@login_required
def ver_perfil(request):
    return render(request, 'accounts/perfil.html') 


class CambiarContraseña(LoginRequiredMixin, PasswordChangeView):
    form_class = NuestroFormularioCambioPassword
    template_name = 'accounts/editar_password.html'
    success_url = reverse_lazy('editar_perfil')

