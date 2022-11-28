from . import views
from django.urls import path

app_name = "gestion_tareas"

urlpatterns =[
    path("", views.index,name="index"),
    path("dashboard",views.dashboard,name= "dashboard"),
    path("vista_tarea/<str:ind>",views.detalleTareas,name="vista_tarea"),
    path("eliminar_tarea/<str:ind>", views.eliminar_tarea, name="eliminar_tarea")
]