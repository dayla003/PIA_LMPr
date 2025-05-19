from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Pelicula

# Create your views here.
def inicio(request):
    return render(request, 'paginas/inicio.html')

def peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/index.html', {'peliculas': peliculas})
