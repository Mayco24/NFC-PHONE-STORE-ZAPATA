from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class NuestroFormularioDeRegistro(UserCreationForm):
    nombre = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    usuario = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Correo Electronico', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['nombre', 'apellido','usuario','email','password1','password2']
        help_texts = {campo: '' for campo in fields}

class NuestroEditarPerfilFormulario(UserChangeForm):
    password = None
    email = forms.EmailField(label = 'Cambiar email', widget=forms.TextInput(attrs={'class':'form-control'}))
    nombre = forms.CharField(label='Nombre', max_length=30, widget=forms.TextInput(attrs={'class':'form-control'}))
    apellido = forms.CharField(label='Apellido', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['email','nombre','apellido']
        help_texts = {campo: '' for campo in fields}

class NuestroFormularioCambioPassword(PasswordChangeForm):
    old_password = forms.CharField(label=("Contraseña Actual"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=("Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(label=("Repita Nueva Contraseña"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')