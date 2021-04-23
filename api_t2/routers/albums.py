from ninja import Router
from typing import List
from ..schemas.artists import ArtistIn, ArtistOut
from ..models.artists import Artist
from ..schemas.albums import AlbumIn, AlbumOut
from ..models.albums import Album
from ..schemas.tracks import TrackIn, TrackOut
from ..models.tracks import Track
from base64 import b64encode
from ninja.errors import HttpError
from django.shortcuts import get_object_or_404


router = Router()


@router.get("", response=List[AlbumOut])
def get_albums(request):
    albums = Album.objects.all()
    return [a.dict() for a in albums]

@router.get("/{album_id}", response=AlbumOut)
def get_album_with_id(request, album_id: str):
    return get_object_or_404(Album, id=album_id).dict()

@router.get("/{album_id}/tracks", response=List[TrackOut])
def get_tracks_of_album(request, album_id: str):
    get_object_or_404(Album, id=album_id)
    tracks = Track.objects.filter(album_id = album_id)
    return [t.dict() for t in tracks]

@router.put("/{album_id}/tracks/play")
def play_tracks_of_album(request, album_id: str):
    album = get_object_or_404(Album, id=album_id)
    tracks = Track.objects.filter(album_id = album_id)
    for track in tracks:
        track.times_played += 1
        track.save()
    return

@router.delete("/{album_id}", response = {204: None})
def delete_album(request, album_id: str):
    delete_count = get_object_or_404(Album, id=album_id).delete()
    # If delete_count is one, we were successful
    return 204

@router.post("/{album_id}/tracks", response={201: TrackOut, 409: TrackOut, 422: None})
def create_track(request, album_id: str, track: TrackIn):
    try:
        referenced_album = Album.objects.get(id=album_id)
    except:
        return 422, None
    else:
        track_id = b64encode(f"{track.name}:{album_id}".encode()).decode('utf-8')
        if len(track_id) > 22:
            track_id = track_id[:22]
        exists = Track.objects.filter(id = track_id)
        if exists:
            return 409, exists[0].dict()
        track_model = Track(id = track_id, 
            album = referenced_album, 
            self_url = f"http://afternoon-citadel-29736.herokuapp.com/api/tracks/{track_id}",
            **track.dict())
        track_model.save()
        return 201, track_model.dict()