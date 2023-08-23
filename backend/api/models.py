from django.db import models
from django.core.exceptions import ValidationError


class Singer(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='название',
        unique=True
    )

    class Meta:
        verbose_name = "Исполнитель"
        verbose_name_plural = "Исполнители"

    def __str__(self) -> str:
        return self.name


class Song(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="название песни",
        unique=True
    )
    order_number = models.IntegerField(
        verbose_name="порядковый номер в альбоме"
    )

    class Meta:
        verbose_name = "Песня"
        verbose_name_plural = "Песни"

    def __str__(self) -> str:
        return self.name


class Album(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="название альбома",
        unique=True
    )
    relise_year = models.DateField(
        verbose_name="дата выпуска"
    )
    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        related_name='albums',
        verbose_name="исполнитель"
    )
    songs = models.ManyToManyField(
        Song,
        through='AlbumSong',
        verbose_name='песни альбома',
    )

    class Meta:
        verbose_name = "Альбом"
        verbose_name_plural = "Альбомы"

    def __str__(self) -> str:
        return self.name


class AlbumSong(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        verbose_name='альбом',
        related_name='albumsongs'
        )
    song = models.ForeignKey(
        Song,
        on_delete=models.CASCADE,
        verbose_name='песня',
        related_name='albumsongs'
    )

    class Meta:
        verbose_name = 'песня в альбоме'
        verbose_name_plural = 'песни в альбоме'

    def validate_unique(self, exclude=None):
        qs = AlbumSong.objects.filter(album=self.album)
        if qs.filter(song__order_number=self.song.order_number).exists():
            raise ValidationError(
                'Песня с таким порядковым номером уже существует в указанном альбоме!'
            )

    def save(self, *args, **kwargs):
        self.validate_unique()
        super(AlbumSong, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.album.name}: {self.song.name}'
