import unittest
from unittest.mock import patch, MagicMock
from .views import fetch_tmdb_data

class TestFetchTmdbData(unittest.TestCase):

    @patch('views.requests.get')
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
        mock_get.assert_called_once_with('mock_url', headers=..., params={'page': 1})

    @patch('views.requests.get')
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
        mock_get.assert_called_once_with('mock_url', headers=...)

    @patch('views.requests.get')
    def test_fetch_tmdb_data_with_request_exception(self, mock_get):
        # Mocking the requests.get function to raise an exception
        mock_get.side_effect = requests.exceptions.RequestException('Mock Request Exception')

        # Calling the function
        result = fetch_tmdb_data(url='mock_url', page=1)

        # Assertions
        self.assertEqual(result, [])

