from . import views
from django.urls import path

app_name = "gestion_tareas"

urlpatterns =[
    path("", views.index,name="index"),
    path("dashboard",views.dashboard,name= "dashboard")
]