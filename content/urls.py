from django.urls import path
from .views import UploadFeed, Profile, Main

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('profile', Profile.as_view()),
    path('main', Main.as_view())
]
