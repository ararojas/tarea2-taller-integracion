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

@router.get("", response=List[TrackOut])
def get_tracks(request):
    tracks = Track.objects.all()
    return [t.dict() for t in tracks]

@router.get("/{track_id}", response=TrackOut)
def get_track(request, track_id: str):
    return get_object_or_404(Track, id=track_id).dict()

@router.put("/{track_id}/play")
def play_track(request, track_id: str):
    track = get_object_or_404(Track, id=track_id)
    track.times_played += 1
    track.save()
    return 

@router.delete("/{track_id}", response = {204: None})
def delete_track(request, track_id: str):
    delete_count = get_object_or_404(Track, id=track_id).delete()
    # If delete_count is one, we were successful
    return 204