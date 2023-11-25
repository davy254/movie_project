# Django IMDb Movie App

## Overview

This is a Django web application that displays a list of latest movies using the TMDb API (The Movie Database). Users can view details of each movie, and the application supports pagination.

## Features

- Display a paginated list of latest movies.
- Show detailed information for each movie.
- Responsive design for a better user experience on various devices.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python (version 3.x)
- Django

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/django-imdb-app.git
    ```

2. Navigate to the project directory:

    ```bash
    cd django-imdb-app
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




