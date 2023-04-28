from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request): #Funcion que crea una solicitud, imprime solo un html
    return render(request, 'paginas/inicio.html')
def nosotros(request): #Funcion que busca un archivo que accede directamente a templates
    return render(request, 'paginas/nosotros.html')

def usuarios(request): 
    return render(request, 'usuario/index.html')
def crear_usuarios(request):
    return render(request, 'usuario/crear.html')