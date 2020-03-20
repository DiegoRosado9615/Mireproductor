from django.contrib import admin

# Register your models here.
from django.contrib import admin
# Models
from .models import Song, Artist

# Register your models here.
admin.site.register(Song)
admin.site.register(Artist)
