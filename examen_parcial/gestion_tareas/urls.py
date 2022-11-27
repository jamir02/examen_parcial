from . import views
from django.urls import path

app_name = "ejemplo_django"

urlpatterns =[
    path("", views.index,name="index")
]