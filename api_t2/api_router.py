from ninja import NinjaAPI
from .routers.artists import router as artist_router
from .routers.albums import router as album_router
from .routers.tracks import router as track_router
from ninja.errors import ValidationError
from django.http import HttpResponse

api = NinjaAPI()


api.add_router("/artists", artist_router, tags=["Artists"])
api.add_router("/albums", album_router, tags=["Albums"])
api.add_router("/tracks", track_router, tags=["Tracks"])

@api.exception_handler(ValidationError)
def validation_errors(request, exc):
    return HttpResponse("Invalid input", status=400)