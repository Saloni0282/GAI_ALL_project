import json
import unittest
from flask import Flask
from app import app

class WeatherDataManagementTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
    
    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "Today, Weather Forecast!")


    def test_create_weather_data(self):
        new_data = {'city': 'Chicago', 'temperature': 18, 'weather': 'Partly Cloudy'}
        response = self.app.post('/weather/', data=json.dumps(new_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)  # 201 Created status code

        # Verify that the new data is added
        response = self.app.get('/weather/Chicago/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['temperature'], 18)
        self.assertEqual(data['weather'], 'Partly Cloudy')

    def test_update_weather_data(self):
        updated_data = {'temperature': 22, 'weather': 'Sunny'}
        response = self.app.put('/weather/New York/', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # Verify that the data is updated
        response = self.app.get('/weather/New York/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['temperature'], 22)
        self.assertEqual(data['weather'], 'Sunny')

    def test_delete_weather_data(self):
        response = self.app.delete('/weather/Los Angeles/')
        self.assertEqual(response.status_code, 204)  # 204 No Content status code

        # Verify that the data is deleted
        response = self.app.get('/weather/Los Angeles/')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()


# import json
# import unittest
# from flask import Flask
# from app import app  # Import the app instance from your app module

# class WeatherViewTest(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()

#     def test_valid_city(self):
#         response = self.app.get('/weather/San Francisco')
#         self.assertEqual(response.status_code, 200)
#         data = json.loads(response.data)
#         self.assertEqual(data['temperature'], 14)
#         self.assertEqual(data['weather'], 'Cloudy')

#     def test_invalid_city2(self):
#         response = self.app.get('/weather/InvalidCity')
#         self.assertEqual(response.status_code, 308)

# if __name__ == '__main__':
#     unittest.main()



# # class BasicTestCase(unittest.TestCase):

# #     def setUp(self):
# #         self.app = app.test_client()

# #     def test_hello_world(self):
# #         response = self.app.get('/')
# #         self.assertEqual(response.status_code, 200)
# #         self.assertEqual(response.data.decode(), "Hello, World!")

# if __name__ == '__main__':
#     unittest.main()
