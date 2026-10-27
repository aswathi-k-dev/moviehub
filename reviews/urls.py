from django.urls import path
from reviews.views import ReviewListCreateView
from reviews.views import ReviewRetrieveUpdateDeleteView

urlpatterns = [
    path("create/<int:pk>/",ReviewListCreateView.as_view()),
    path("<int:pk>/",ReviewRetrieveUpdateDeleteView.as_view()),



]