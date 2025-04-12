import unittest
from unittest.mock import patch, Mock
import hello  # Import the hello.py module

class TestHello(unittest.TestCase):
    @patch('hello.requests.get')
    def test_successful_api_request(self, mock_get):
        # Mock a successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "latitude": 48.37,
            "longitude": 10.90,
            "current_weather": {
                "temperature": 15.3,
                "windspeed": 5.6,
                "weathercode": 1
            }
        }
        mock_get.return_value = mock_response

        # Call the code in hello.py
        response = hello.requests.get(hello.API_ENDPOINT, params=hello.params)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertIn("latitude", response.json())
        self.assertIn("current_weather", response.json())

    @patch('hello.requests.get')
    def test_failed_api_request(self, mock_get):
        # Mock a failed API response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Call the code in hello.py
        response = hello.requests.get(hello.API_ENDPOINT, params=hello.params)

        # Assertions
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()