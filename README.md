# Django TMDb Movie App
[![Django CI](https://github.com/davy254/movie_project/actions/workflows/django.yml/badge.svg)](https://github.com/davy254/movie_project/actions/workflows/django.yml)
## Overview

This is a Django web application that displays a list of latest movies using the TMDb API (The Movie Database). Users can view details of each movie.

## Features

- Display a paginated list of latest movies.
- Show detailed information for each movie.
- Responsive design for a better user experience on various devices.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (version 3.10)
- Django (version 4.2)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/davy254/movie_project
    ```

2. Navigate to the project directory:

    ```bash
    cd movie_project
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the application in your web browser at `http://localhost:8000`.

### Configuration

1. Obtain a TMDb API key from [TMDb API](https://www.themoviedb.org/settings/api).
2. Replace the placeholder API key in the `latest_movies` view in `views.py` with your actual TMDb API key.

    ```python
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer YOUR_TMDB_API_KEY"
    }
    ```

## Usage

1. Visit the homepage to see the list of latest movies.
2. Click on a movie to view its details.




