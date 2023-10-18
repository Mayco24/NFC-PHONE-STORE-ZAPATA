from django.urls import path
from InicioProject.views import inicio, publicar_equipos , listado_equipos, editar_equipos, eliminar_equipos, detalles_equipos, acerca_de_mi

urlpatterns = [
    path("", inicio, name="inicio"),
    #path("registrar-devices/<str:titulo>/<str:marca>/<str:modelo>/<int:cantidad>/", registrar_devices, name= "registrar_devices"),
    path("equipos", listado_equipos, name= "equipos"),
    path("PublicarEquipo", publicar_equipos, name= "publicar_equipos"),
    path('equipos/<int:id_equipos>detalles/', detalles_equipos , name='detalles_equipos'),
    path('equipos/<int:id_equipos>editar/', editar_equipos, name='editar_equipos'),
    path('equipos/<int:id_equipos>eliminar/', eliminar_equipos, name='eliminar_equipos'),
    path("about/", acerca_de_mi, name="acerca_de_mi")
]
