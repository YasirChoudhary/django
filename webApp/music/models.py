from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=210)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return ("artist={} , album_title={}".format(self.artist,self.album_title))

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE )
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return ("songtitle = {}".format(self.song_title))