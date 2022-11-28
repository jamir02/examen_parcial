from django.shortcuts import render
from django.http import HttpResponse
from .models import usuario
from .models import tarea
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

usuarios_totales = usuario.objects.all() # Traigo todos los usuarios de la base de datos


# Funcion de login
def index(request):
    tareas_totales= tarea.objects.all()
    if request.method =="POST":
        usuario = request.POST.get("usuario") # Obtengo el usuario de la vista
        contrasena = request.POST.get("contrasena") #Obtengo contraseña de la vista
        for each_usuario in usuarios_totales: # Comprueba para cada usuario
            if ((each_usuario.nombre == usuario) and (each_usuario.clave == contrasena)): # Compruebo credenciales
                print("Ingreso valido")
                print("El nombre de usuario es: " + str(usuario))
                print("La contraseña del usuario es: " + str(contrasena)) # Se immprime el usuario y contraseña
                return HttpResponseRedirect(reverse("gestion_tareas:dashboard")) #Voy a la vista dashboard
    return render(request,"gestion_tareas/ingreso.html") # Caso contrario retorna la vista de login 
def dashboard(request):
    tareas_totales= tarea.objects.all() #Traigo todas las tareas de la base de datos
    if request.method == "POST":
        titulo= request.POST.get('titulotarea')#Recibo el titulo de la nueva tarea
        descripcion= request.POST.get('descripciontarea')#Recibo la descripcion de la nueva tarea
        fecha_creacion= request.POST.get('fechacreaciontarea') #Recibo la fecha de la creacion de la nueva tarea
        fecha_entrega= request.POST.get('fechaentregatarea') #Recibo la fecha de entrega de la nueva tarea
        usuario_designado= request.POST.get('usuariodesignadotarea') #Recibo el usuario designado de la nueva tarea
        tarea(titulo=str(titulo), descripcion=str(descripcion),fecha_creacion=str(fecha_creacion),fecha_entrega=str(fecha_entrega),usuario_designado=str(usuario_designado)).save() #Lo guardo en la base de datos
    return render(request,"gestion_tareas/dashboard.html",{ #Retorna la vista de dashboard
        'tareas_totales': tareas_totales # entrega la lista de tareas totales a la vista
    })

def detalleTareas(request, ind):
    tarea_seleccionada=tarea.objects.get(id=ind) #Obtenemos la tarea seleccionada
    return render(request,"gestion_tareas/vista_tarea.html",{ #Redirecciono a la vista de la tarea brindando la info de la tarea extraida de la base de datos
        "tarea_seleccionada":tarea_seleccionada
    })
def eliminar_tarea(request,ind):
    tarea_eliminar = tarea.objects.get(id=ind)#Obtengo la tarea seleccionada por id 
    tarea_eliminar.delete() #Elimino la tarea seleccionada de la base de datos
    return HttpResponseRedirect(reverse("gestion_tareas:dashboard"))#Redirecciono a la vista de dashboard
