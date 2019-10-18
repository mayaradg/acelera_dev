from django.contrib import admin
from .models import Genre, Movie

admin.register(*(Genre, Movie))
