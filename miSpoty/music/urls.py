from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('cancionesPopulares/', views.cancionesPopulares,name="cancionesPopulares"),
    path('player/', views.playerMusic,name="reproductorMusical")

]
