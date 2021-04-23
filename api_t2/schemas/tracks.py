from ninja import Schema

class TrackIn(Schema):
    name: str
    duration: float


class TrackOut(Schema):
    id: str
    album_id: str
    name: str
    duration: float
    times_played: int
    artist: str
    album: str
    self: str