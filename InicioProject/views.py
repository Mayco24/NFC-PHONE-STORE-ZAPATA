from django.shortcuts import render, redirect
from django.template import Template, Context
from django.http import HttpResponse
from datetime import datetime
from InicioProject.models import Equipos
from InicioProject.forms import Crear_EquiposFormulario, Editar_EquiposFormulario, EquiposBusquedaFormularios
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):

    datos = {
        'fecha': datetime.now()
    }

    return render(request, r'inicio\inicio.html', datos)

def acerca_de_mi(request):
    datos = {
        'fecha': datetime.now()
    }
    return render(request, r'inicio\acerca_de_mi.html', datos )

def publicar_equipos(request):

    if request.method == 'POST':
        formulario = Crear_EquiposFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            devices = Equipos(titulo=data.get('titulo'), marca=data.get('marca'), modelo=data.get('modelo'),  estado=data.get('estado'), precio=data['precio'])
            devices.save()
            return redirect('equipos')
        else:
            return render(request, r'inicio\publicar_equipo.html', {'formulario': formulario})
            
    formulario = Crear_EquiposFormulario()
    return render(request, r'inicio\publicar_equipo.html', {'formulario': formulario})

@login_required
def editar_equipos(request, id_equipos):

    equipos_a_editar = Equipos.objects.get(id= id_equipos)

    if request.method == 'POST':
        formulario = Editar_EquiposFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            equipos_a_editar.titulo = data['titulo']
            equipos_a_editar.marca = data['marca']
            equipos_a_editar.modelo = data['modelo']
            equipos_a_editar.estado = data['estado']
            equipos_a_editar.precio = data['precio']
            equipos_a_editar.save()
        else:
            return render(request, r'inicio\editar_equipo.html', {'formulario': formulario})
        
    formulario = Editar_EquiposFormulario(initial={'titulo': equipos_a_editar.titulo, 'marca': equipos_a_editar.marca, 'modelo': equipos_a_editar.modelo, 'estado': equipos_a_editar.estado, 'precio': equipos_a_editar.precio})
    return render(request, r'inicio\editar_equipo.html', {'formulario': formulario})

@login_required
def eliminar_equipos(request,id_equipos):

    equipos_a_eliminar = Equipos.objects.get(id= id_equipos)
    equipos_a_eliminar.delete()

    return redirect('equipos')

def detalles_equipos(request,id_equipos):
    equipo = Equipos.objects.get(id=id_equipos)
    return render(request, 'inicio/detalle_equipo.html', {'equipo': equipo})

def listado_equipos(request):
    
    formulario = EquiposBusquedaFormularios(request.GET)
    if formulario.is_valid():
        titulo_a_buscar = formulario.cleaned_data.get('titulo')
        equipos_encontrados = Equipos.objects.filter(titulo__icontains=titulo_a_buscar)
    else:
        equipos_encontrados = Equipos.objects.all()
    
    formulario = EquiposBusquedaFormularios()
    return render(request, r'inicio\listado_equipos.html', {'formulario': formulario, 'equipos_encontrados': equipos_encontrados})
