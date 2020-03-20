from django.urls import path
from .models import *
from .views import *
urlpatterns=[
    path('',home ),
    path('cancionesPopulares/', cancionesPopulares),
    path('player/',playerMusic)
]
