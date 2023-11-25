from django.urls import path
from .views import latest_movies


app_name = 'movie_app'
urlpatterns = [
    path('', latest_movies, name='latest-movies')
]
