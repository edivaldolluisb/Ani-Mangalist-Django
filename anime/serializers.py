from rest_framework import serializers
from .models import Anime, Manga, Autor, Estudio


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class EstudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudio
        fields = '__all__'


class AnimeSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    estudio = EstudioSerializer(many=True)

    class Meta:
        model = Anime
        fields = '__all__'


class MangaSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    class Meta:
        model = Manga
        fields = '__all__'


