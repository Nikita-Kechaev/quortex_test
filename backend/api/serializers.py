from rest_framework import serializers

from .models import Album, Singer, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    singer = serializers.StringRelatedField()
    songs = SongSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'


class SingerSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True)

    class Meta:
        model = Singer
        fields = '__all__'
