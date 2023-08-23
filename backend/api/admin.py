from django.contrib import admin

from .models import Album, Singer, Song, AlbumSong


@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "singer"
    )


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )


@admin.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    list_display = (
        "album",
        "song"
    )
