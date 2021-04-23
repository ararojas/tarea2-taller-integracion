from ninja import NinjaAPI
from .routers.artists import router as artist_router
from .routers.albums import router as album_router
from .routers.tracks import router as track_router

api = NinjaAPI()

api.add_router("/artists", artist_router, tags=["Artists"])
api.add_router("/albums", album_router, tags=["Albums"])
api.add_router("/tracks", track_router, tags=["Tracks"])