from django.urls import path
from films.views import SignUpView
from rest_framework.authtoken.views import ObtainAuthToken
from films.views import MovieListView
from films.views import MovieCreateView
from films.views import MovieRetrieveUpdateDeleteView



urlpatterns = [
    path("register/",SignUpView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
    path('movies/',MovieListView.as_view()),
    path('movies/create/',MovieCreateView.as_view()),
    path('movies/',MovieRetrieveUpdateDeleteView.as_view()),   
]