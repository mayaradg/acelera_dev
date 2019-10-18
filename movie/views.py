from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre

# Create your views here.


class MovieViewSet(ModelViewSet):
    lookup_field = "pk"
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreViewSet(ModelViewSet):
    lookup_field = "pk"
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
