from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre

# Create your views here.


class MovieViewSet(ModelViewSet):
    lookup_field = "pk"
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    @action(detail=True, methods=["get"])
    # I coded this as GET because it's easier to see it in browsable API but this should be a POST
    def increase(self, request, pk):
        movie = self.get_object()
        movie.times_watched += 1
        movie.save()
        data = MovieSerializer(instance=movie).data
        return Response(data=data, status=status.HTTP_200_OK)


class GenreViewSet(ModelViewSet):
    lookup_field = "pk"
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
