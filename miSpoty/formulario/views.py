from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from formulario.forms import SingUpForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login,logout


# Create your views here.
class SignUp (View):
    template= "formulario/Registro.html"
    """Nuevo usuario."""
    def get(self, request):

        """Render sign up form."""
        form = SingUpForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):


        """Receive and validate sign up form."""
        form = SingUpForm(request.POST)
        ##print(from.is_valid())
        if not form.is_valid():
            print("Entre a este caso y el error es este")
            print(form.errors)
            context = {"form": form}
            return render(request, self.template, context)

        new_user = User.objects.create_user(
        username=form.cleaned_data["email"],
        email=form.cleaned_data["email"],
        password=form.cleaned_data["password"],
        first_name=form.cleaned_data["primer_nombre"],
        last_name=form.cleaned_data["apellido"],
        )
        print("Ganamos")
        return HttpResponse("<h1>usuarioCreado!</h1>")


class Login(View):
    """New User Sign Up."""

    template = "formulario/Login.html"

    def get(self, request):
        """Render sign up form."""
        form = LoginForm()
        context = {"form": form}
        return render(request, self.template, context)

    def post(self, request):
        """Receive and validate sign up form."""
        form = LoginForm(data=request.POST)

        if not form.is_valid():
            context = {"form": form}
            return render(request, self.template, context)

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        login(request, user)

        return HttpResponse("<h1>User logged!</h1>")

class LogOut(View):
    """docstring for ."""
    def get(self,request):
        logout(request)
        return redirect ("music:home")
