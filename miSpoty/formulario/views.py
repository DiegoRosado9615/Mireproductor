from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from formulario.forms import SingUpForm

# Create your views here.
class Artista (View):
    template= "Registro.html"
    """Nuevo usuario."""
    def get(self, request):
        """Render sign up form."""
        form = SingUpForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        """Receive and validate sign up form."""
        form = SignUpForm(request.POST)
        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)

        new_user = User.objects.create_user(
        username=form.cleaned_data["email"],
        email=form.cleaned_data["email"],
        password=form.cleaned_data["password"],
        first_name=form.cleaned_data["first_name"],
        last_name=form.cleaned_data["last_name"],
        )

        return HttpResponse("<h1>usuarioCreado!</h1>")
