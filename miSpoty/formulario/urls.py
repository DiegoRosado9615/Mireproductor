from django.urls import include,path
from django.contrib import admin
from .models import *
from .views import *
from django.contrib.auth import authenticate, login

from formulario import views

app_name = "formulario"
urlpatterns = [
    path("registro/", views.SignUp.as_view(), name="registro"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.LogOut.as_view(), name="logout"),

]
