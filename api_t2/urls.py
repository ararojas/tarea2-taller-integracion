from django.urls import path
from .api_router import api

urlpatterns = [
    path("", api.urls),
]