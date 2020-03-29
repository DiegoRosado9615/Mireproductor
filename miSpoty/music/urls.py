from django.urls import path
from .models import *
from .views import *
from music import views

app_name = "music"
urlpatterns=[

    path('',home, name="home") ,
    path('cancionesPopulares/', cancionesPopulares),
    path('player/',playerMusic),
    path("Artista/",views.crearArtista.as_view(),name="addArtista"),
]
