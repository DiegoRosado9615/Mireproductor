from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.views import View
from music.forms import crearArtista
from django.http import HttpResponse
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index (request):
    return HttpResponse("Bienvenidos")

def home(request):
    context={}
    return render(request,'music/home.html',context)

def cancionesPopulares(request):
    if request.method == 'GET':
        songs = Song.objects.all()
        to_play_id = request.GET.get("to_play", 1)
        songs_to_play = Song.objects.filter(id=to_play_id)
        if songs_to_play.count() == 0:
            to_play = Song.objects.first()
        else:
            to_play = songs_to_play.first()

        context = {"songs": songs, "to_play": to_play}
        return render(request, 'music/index.html', context)

def playerMusic(request):
    context={}
    return render(request,'music/player.html',context)


class crearArtista(View):
    def get(self, request):
        form = crearArtista()
        context = {"form": form}
        return render(request, 'music/Artista.html', context)
    def post(self, request):
        form = crearArtista(request.POST, request.FILES)
        print(form)
        if not form.is_valid():
            context = {"form": form}
            return render(request, 'music/Artista.html', context)
        Artist.objects.create(
        name=form.cleaned_data["name"],
        image=form.cleaned_data["image"],)
        return render(request, 'music/home.html')


def get(self, request):
        """GET method."""
        form=Artist()
        context={"form":form}
        return render(request, self.template,context)
