from django.urls import path
from music.views import SongCreateView
from music.views import SongRetrieveUpdateDeleteView

urlpatterns = [
    path("movies/<int:pk>/song/",SongCreateView.as_view()),
    path("movies/song/<int:pk>/",SongRetrieveUpdateDeleteView.as_view()),

]