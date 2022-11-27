from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario
# Create your views here.

usuarios_totales = usuario.objects.all() # Traigo todos los usuarios de la base de datos

# Funcion de login
def index(request):
    if request.method =="POST":
        usuario = request.POST.get("usuario") # Obtengo el usuario de la vista
        contrasena = request.POST.get("contrasena") #Obtengo contraseña de la vista
        for each_usuario in usuarios_totales: # Comprueba para cada usuario
            if ((each_usuario.nombre == usuario) and (each_usuario.clave == contrasena)): # Compruebo credenciales
                print("Ingreso valido")
                print("El nombre de usuario es: " + str(usuario))
                print("La contraseña del usuario es: " + str(contrasena)) # Se immprime el usuario y contraseña
                return render(request,"gestion_tareas/dashboard.html") # Retorna la vista de dashboard

    return render(request,"gestion_tareas/ingreso.html") # Caso contrario retorna la vista de login 
def dashboard(request):
    return render(request,"gestion_tareas/dashboard.html")


