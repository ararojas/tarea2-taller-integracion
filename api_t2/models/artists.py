from django.db import models


class Artist(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=22, unique = True)
    artist_id = models.CharField(max_length=4096)
    name = models.CharField(max_length=256)
    age = models.IntegerField()
    albums = models.CharField(max_length=4096)
    tracks = models.CharField(max_length=4096)
    self_url = models.CharField(max_length=4096)

    def dict(self):
        return {'id': self.id,
        'name': self.name,
        'age': self.age,
        'albums': self.albums,
        'tracks': self.tracks,
        'self': self.self_url}
