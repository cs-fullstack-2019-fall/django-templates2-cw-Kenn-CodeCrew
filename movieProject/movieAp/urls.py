from django.urls import path
from . import views

urlpatterns = [
    path("movie_synopsis/<int:movieID>/", views.movie_synopsis, name="movie_synopsis"),
    path("movie_details/<int:movieID>/", views.movie_details, name="movie_details"),
    path("", views.index, name="index"),
]