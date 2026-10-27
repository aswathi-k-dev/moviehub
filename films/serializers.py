from rest_framework import serializers
from films.models import Movie
from music.models import Song
from music.serializers import SongSerializer

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","email","password"]


class MovieSerializer(serializers.ModelSerializer):

    song_count = serializers.SerializerMethodField(read_only=True)
    songs = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ["id","created_by","created_at"]

    def get_song_count(self, obj):
        return Song.objects.filter(movie=obj).count()

    def get_songs(self, obj):
        song_object = Song.objects.filter(movie=obj)

        serializer_instance = SongSerializer(song_object,many=True)

        return serializer_instance.data
