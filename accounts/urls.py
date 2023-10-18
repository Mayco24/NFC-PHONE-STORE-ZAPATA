from django.urls import path
from accounts.views import login, registro, editar_perfil, CambiarContraseña, ver_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login, name='login'),
    path('registrarse/', registro , name='registro'),
    path('perfil/editar/', editar_perfil , name='editar_perfil'),
    path('perfil/editar/contraseña', CambiarContraseña.as_view() , name='editar_password'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html', next_page='login'), name='logout')
]
