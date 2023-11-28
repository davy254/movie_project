import unittest
from unittest.mock import patch, MagicMock

import requests
from movie_app.views import fetch_tmdb_data

bearer_token = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ZDVlNDlkNzQyNDVkNGZiNzg1YTc0YjY1NzI3ZWZkNCIsInN1YiI6IjY1NTQ3Y2I3NTM4NjZlMDBhYmFhYTAwYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.uNLKtu3ip1TMnNrN5RPKkEYcDJXI-X2d_qrp_AdGNoE"

class TestFetchTmdbData(unittest.TestCase):

    @patch('movie_app.views.requests.get')
    def test_fetch_tmdb_data_with_results(self, mock_get):
        # Mocking the requests.get function
        mock_response = MagicMock()
        mock_response.json.return_value = {'results': [{'title': 'Movie 1'}, {'title': 'Movie 2'}]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Calling the function
        result = fetch_tmdb_data(url='mock_url', page=1)

        # Assertions
        self.assertEqual(result, [{'title': 'Movie 1'}, {'title': 'Movie 2'}])
        mock_get.assert_called_once_with('mock_url', headers={'accept': 'application/json', 'Authorization': bearer_token}, params={'page': 1})

    @patch('movie_app.views.requests.get')
    def test_fetch_tmdb_data_with_movie_id(self, mock_get):
        # Mocking the requests.get function
        mock_response = MagicMock()
        mock_response.json.return_value = {'title': 'Mock Movie'}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        # Calling the function
        result = fetch_tmdb_data(url='mock_url', movie_id='mock_movie_id')

        # Assertions
        self.assertEqual(result, {'title': 'Mock Movie'})
        mock_get.assert_called_once_with('mock_url', headers={'accept': 'application/json', 'Authorization': bearer_token})

    @patch('movie_app.views.requests.get')
    def test_fetch_tmdb_data_with_request_exception(self, mock_get):
        # Mocking the requests.get function to raise an exception
        mock_get.side_effect = requests.exceptions.RequestException('Mock Request Exception')

        # Calling the function
        result = fetch_tmdb_data(url='mock_url', page=1)

        # Assertions
        self.assertEqual(result, [])

