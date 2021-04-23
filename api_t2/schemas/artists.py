from ninja import Schema

class ArtistIn(Schema):
    name: str
    age: int


class ArtistOut(Schema):
    id: str
    name: str
    age: int
    albums: str
    tracks: str
    self: str

