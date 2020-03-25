from django.urls import include,path
from django.contrib import admin
from .models import *
from .views import *
from formulario import views

app_name = "formulario"
urlpatterns = [
    path("registro/", views.Artista.as_view(), name="registro"),

]
