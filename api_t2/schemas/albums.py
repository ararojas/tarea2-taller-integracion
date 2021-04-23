from ninja import Schema

class AlbumIn(Schema):
    name: str
    genre: str


class AlbumOut(Schema):
    id: str
    artist_id: str
    name: str
    genre: str
    artist: str
    tracks: str
    self: str