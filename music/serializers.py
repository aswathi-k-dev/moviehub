from rest_framework import serializers
from music.models import Song


class SongSerializer(serializers.ModelSerializer):

    class Meta:
        model = Song
        fields = "__all__"

        read_only_fields = ["id","movie","track_number","created_by","created_at"]