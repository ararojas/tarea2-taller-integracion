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


@router.post("", response = {201: ArtistOut, 409: ArtistOut})
def create_artist(request, artist: ArtistIn):
    artist_id = b64encode(artist.name.encode()).decode('utf-8')
    if len(artist_id) > 22:
        artist_id = artist_id[:22]
    exists = Artist.objects.filter(id = artist_id)
    if exists:
        return 409, exists[0].dict()
    artist_model = Artist(id = artist_id, 
    name = artist.name, 
    age = artist.age,
    albums = f"http://[::1]:8000/api/artists/{artist_id}/albums",
    tracks = f"http://[::1]:8000/api/artists/{artist_id}/tracks",
    self_url = f"http://[::1]:8000/api/artists/{artist_id}")
    artist_model.save()
    return 201, artist_model.dict()

@router.post("/{artist_id}/albums", response={201: AlbumOut, 409: AlbumOut, 422: None})
def create_album(request, artist_id: str, album: AlbumIn):
    try:
        referenced_artist = Artist.objects.get(id=artist_id)
    except:
        return 422, None
    else:
        album_id = b64encode(f"{album.name}:{artist_id}".encode()).decode('utf-8')
        if len(album_id) > 22:
            album_id = album_id[:22]
        exists = Album.objects.filter(id = album_id)
        if exists:
            return 409, exists[0].dict()
        album_model = Album(id = album_id, 
            artist = referenced_artist, 
            tracks = f"http://[::1]:8000/api/albums/{album_id}/tracks",
            self_url = f"http://[::1]:8000/api/albums/{album_id}",
            **album.dict())
        album_model.save()
        return 201, album_model.dict()

@router.get("", response=List[ArtistOut])
def get_artists(request):
    artists = Artist.objects.all()
    return [a.dict() for a in artists]

@router.get("/{artist_id}", response=ArtistOut)
def get_artist(request, artist_id: str):
    return get_object_or_404(Artist, id=artist_id).dict()

@router.get("/{artist_id}/albums", response=List[AlbumOut])
def get_albums_by_artist(request, artist_id: str):
    get_object_or_404(Artist, id=artist_id)
    albums = Album.objects.filter(artist_id = artist_id)
    return [a.dict() for a in albums]

@router.get("/{artist_id}/tracks", response=List[TrackOut])
def get_tracks_by_artist(request, artist_id: str):
    get_object_or_404(Artist, id=artist_id)
    albums = Album.objects.filter(artist_id = artist_id)
    tracks = []
    for album in albums:
        tracks += Track.objects.filter(album_id = album.id)
    return [t.dict() for t in tracks]

@router.put("/{artist_id}/albums/play")
def play_tracks_of_artist(request, artist_id: str):
    get_object_or_404(Artist, id=artist_id)
    albums = Album.objects.filter(artist_id = artist_id)
    for album in albums:
        tracks = Track.objects.filter(album_id = album.id)
        for track in tracks:
            track.times_played += 1
            track.save()
    return

@router.delete("/{artist_id}", response = {204: None})
def delete_artist(request, artist_id: str):
    delete_count = get_object_or_404(Artist, id=artist_id).delete()
    # If delete_count is one, we were successful
    return 204