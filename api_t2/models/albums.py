from django.db import models
from ..models.artists import Artist

class Album(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=22, unique = True)
    name = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    tracks = models.CharField(max_length=4096)
    self_url = models.CharField(max_length=4096)

    def dict(self):
        return {'id': self.id,
        'artist_id': self.artist.id,
        'name': self.name,
        'genre': self.genre,
        'artist': self.artist.self_url, #not sure
        'tracks': self.tracks,
        'self': self.self_url}