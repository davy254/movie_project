# movies/views.py
import json
from django.shortcuts import render
from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests


def latest_movies(request):
    """
    Function for getting latest movies 
    """
    movies = None
    pages = 2
    for page in range(1,pages + 1):
        url = "https://api.themoviedb.org/3/movie/now_playing"
        print(f'page is {page}')

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZDVlNDlkNzQyNDVkNGZiNzg1YTc0YjY1NzI3ZWZkNCIsInN1YiI6IjY1NTQ3Y2I3NTM4NjZlMDBhYmFhYTAwYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.uNLKtu3ip1TMnNrN5RPKkEYcDJXI-X2d_qrp_AdGNoE"
        }

        params = {
            'page': page,
        }

        response = requests.get(url, headers=headers, params=params)
        movie_data = json.loads(response.content)
        if movies == None:
            movies = movie_data.get('results', [])
        else:
            movies.extend(movie_data.get('results'))

    print(movies)
    context = {'latest_movie': movies}
    return render(request, 'movie_app/index.html', context)

