from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.db import models
from django import forms

from .models import *

class SingUpForm(forms.Form):
    primer_nombre=forms.CharField(max_length=200)
    apellido=forms.CharField(max_length=200)
    email=forms.EmailField(max_length=200)
    password=forms.CharField(widget=forms.PasswordInput())
    def clean_email(self):
        """Validate that the email doesn't exist in the database."""
        data = self.cleaned_data["email"]
        if User.objects.filter(email=data).count() > 0:
            raise forms.ValidationError("El email ya existe .")
        return data


class LoginForm(AuthenticationForm):
    """Login form."""

    def clean(self):
        """Validate data.
        Validating all fields.
        """
        username = self.data["username"]
        password = self.data["password"]

        if User.objects.filter(username=username).count() == 0:
            self.add_error(
                "username", forms.ValidationError("El email no existe.")
            )
