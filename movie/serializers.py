from rest_framework.serializers import ModelSerializer
from .models import Genre, Movie


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = "__all__"

