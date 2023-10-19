import json
import unittest
from flask import Flask
from app import app

class WeatherViewTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_valid_city(self):
        response = self.app.get('/weather/San%20Francisco', follow_redirects=False)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(data['temperature'], 14)
        self.assertEqual(data['weather'], 'Cloudy')

    def test_invalid_city(self):
        response = self.app.get('/weather/InvalidCity', follow_redirects=False)
        self.assertEqual(response.status_code, 404)
        response_data = response.data.decode('utf-8')
        self.assertEqual(response_data, 'City not found')

if __name__ == '__main__':
    unittest.main()

#     def test_get_dishes():
#         response=self.app.get("/get_dishes")
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(response.get_json(),list)

# if __name__ == '__main__':
#     unittest.main()
