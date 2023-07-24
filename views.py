from django.shortcuts import render, redirect
from .models import *



# Create your views here.

def main (request):
    return render(request, 'videos/main.html',{})


def mostrar_formulario(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        id = request.POST['id']
        nombre = request.POST['nombre']
        cantidad_videos = request.POST['cantidad_videos']
        confirmacion = {
            'id_nomina': id,
            'nombre': nombre,
            'cantidad_videos': cantidad_videos,
        }

        # Guardar los datos en la base de datos
        usuario = Usuario.objects.create(
            id=id,
            nombre=nombre
            
        )
        usuario.save()

    else:
        confirmacion = None

    return render(request, 'videos/main.html', {'confirmacion': confirmacion})
