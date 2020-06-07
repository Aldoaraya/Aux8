from django.shortcuts import render
from .forms import *

# Create your views here.
def formulario(request):
	form = Formulario()
	return render(request, 'myapp/formulario.html',{'form':form})

def jumbotron(request):
    return render(request,'myapp/jumbotron.html')

def carousel(request):
	return render(request, 'myapp/carousel.html')

def album(request):
	return render(request, 'myapp/album.html')

def signin(request):
        form = Formulario_desafio()
	return render(request,'myapp/sign-in.html',{'form':form})

def resultados(request):
	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	edad = request.POST['edad']
	password = request.POST['password']
	email = request.POST['email']
	contexto = {'nombre':nombre,
				'edad':edad,
				'apellido':apellido,
				'password':password,
				'email':email
				}
	if(edad == '42'):
		contexto['respuesta'] = "la respuesta del universo!!!!!"
	
	return render(request, 'myapp/resultados.html',contexto)

def resultados_desafio(request):
        nombre_usuario = request.POST['nombre_usuario']
        numero_favorito = request.POST['numero_favorito']
        correo = request.POST['correo']
        contraseña = request.POST['contraseña']
        confirmar_contraseña = request.POST['confirmar_contraseña']
        animal_favorito = request.POST['animal_favorito']
        contexto = {'nombre_usuario':nombre_usuario,
				'numero_favorito':numero_favorito,
				'correo':correo,
				'contraseña':contraseña,
				'confirmar_contraseña':confirmar_contraseña,
                                'animal_favorito':animal_favorito                    
				}
        
        if(contraseña != confirmar_contraseña):
                contexto['respuesta'] = "Por favor vuelva a confirmar contraseña"

        return render(request, 'myapp/resultados_desafio.html',contexto)

