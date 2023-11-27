import json
import logging
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests


logger = logging.getLogger(__name__)

def fetch_tmdb_data(*args, **kwargs):
    """
    fetch data from The movie Db
    """
    url = kwargs.get('url')
    page = kwargs.get('page')
    movie_id = kwargs.get('movie_id')

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZDVlNDlkNzQyNDVkNGZiNzg1YTc0YjY1NzI3ZWZkNCIsInN1YiI6IjY1NTQ3Y2I3NTM4NjZlMDBhYmFhYTAwYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.uNLKtu3ip1TMnNrN5RPKkEYcDJXI-X2d_qrp_AdGNoE"
    }

    params = {
        'page': page,
    }

    try:
        if movie_id:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise HTTPError for bad responses
            movie_data = response.json()
            return movie_data
        else:
            response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses
        movie_data = response.json()
        return movie_data.get('results', [])
    except requests.exceptions.RequestException as e:
        # Handle exception (e.g., log the error, provide a default response)
        logger.error(f"Error fetching TMDb data: {e}")
        return []
    
def latest_movies(request):
    """
    Function for dispaying the latest movies 
    """
    url = "https://api.themoviedb.org/3/movie/now_playing"
    movies = []

    # Fetch TMDb data dynamically until no more results
    page = 1
    while True:
        logger.debug(f'Fetching page {page} from TMDb API')
        page_data = fetch_tmdb_data(page=page, url=url)

        if not page_data:
            # No more results, break out of the loop
            break

        movies.extend(page_data)
        page += 1

    # Display movies per page
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

    context = {'latest_movies': current_page}
    return render(request, 'movie_app/index.html', context)    



def movie_detail(request, movie_id):
        """
        Movie to display details of a movie
        """
        url = f'https://api.themoviedb.org/3/movie/{movie_id}'
        movie_data = fetch_tmdb_data(url=url, movie_id = movie_id)
        context = {'movie':movie_data}

        return render(request,'movie_app/movie_detail.html', context)
