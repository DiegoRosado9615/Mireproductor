from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index (request):
    return HttpResponse("Bienvenidos")

def home(request):
    context={}
    return render(request,'music/home.html',context)

def cancionesPopulares(request):
    context={}
    return render(request,'music/index.html',context)

def playerMusic(request):
    context={}
    return render(request,'music/player.html',context)
