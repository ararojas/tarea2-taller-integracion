from django.db import models
from ..models.albums import Album

class Track(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=22, unique = True)
    name = models.CharField(max_length=256)
    duration = models.FloatField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    times_played = models.IntegerField(default = 0, editable = True)
    self_url = models.CharField(max_length=4096)

    def dict(self):
        return {'id': self.id,
        'album_id': self.album.id,
        'name': self.name,
        'duration': self.duration,
        'times_played': self.times_played,
        'artist': self.album.artist.self_url, #not sure
        'album': self.album.self_url,
        'self': self.self_url}