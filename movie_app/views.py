# movies/views.py
import json
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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


    # Dispaly movies per page
    movies_per_page = 36

    paginator = Paginator(movies, movies_per_page)

    page_number = request.GET.get('page')
    try:
        current_page = paginator.get_page(page_number)
    except PageNotAnInteger:
        # If the page parameter is not an integer, deliver the first page
        current_page = paginator.get_page(1)
    except EmptyPage:
        # If the page is out of range (e.g., 9999), deliver the last page
        current_page = paginator.get_page(paginator.num_pages)
    print(current_page)
    context = {'latest_movie': current_page}
    return render(request, 'movie_app/index.html', context)

