import unittest
from unittest.mock import patch, Mock
from main import get_random_cat_image
import requests


class TestGetRandomCatImage(unittest.TestCase):
    @patch("requests.get")
    def test_successful_request(self, mock_get):
        """Тест успешного запроса и возврата URL."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"url": "https://example.com/cat.jpg"}]
        mock_get.return_value = mock_response

        result = get_random_cat_image()
        self.assertEqual(result, "https://example.com/cat.jpg")

    @patch("requests.get")
    def test_failed_request_404(self, mock_get):
        """Тест неуспешного запроса (404) и возврата None."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_get.return_value = mock_response

        result = get_random_cat_image()
        self.assertIsNone(result)

    @patch("requests.get")
    def test_request_exception_returns_none(self, mock_get):
        """Тест обработки исключения при запросе (возвращает None)."""
        mock_get.side_effect = requests.RequestException("Connection Error")

        result = get_random_cat_image()
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()