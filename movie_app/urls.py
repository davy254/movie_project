from django.urls import path
from .views import latest_movies, movie_detail


app_name = 'movie_app'
urlpatterns = [
    path('', latest_movies, name='latest-movies'),
    path('movie-detail/<int:movie_id>', movie_detail, name='movie-detail'),
]
