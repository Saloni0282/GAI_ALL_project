# # app.py
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)

# Define the weather data dictionary outside of the route handlers
weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

@app.route("/")
def hello_world():
     return "Today, Weather Forecast!"

@app.route('/weather/<string:city>/', methods=['GET'])
def get_weather_by_city(city):
    weather_info = weather_data.get(city)
    if weather_info:
        return jsonify(weather_info)
    else:
        return make_response(jsonify({"error": "City not found"}), 404)

@app.route('/weather/', methods=['POST'])
def create_weather_data():
    data = request.get_json()
    if not data or 'city' not in data or 'temperature' not in data or 'weather' not in data:
        return make_response(jsonify({"error": "Invalid data format"}), 400)

    city = data['city']
    temperature = data['temperature']
    weather = data['weather']

    if city in weather_data:
        return make_response(jsonify({"error": "City already exists"}), 400)

    weather_data[city] = {'temperature': temperature, 'weather': weather}
    return make_response(jsonify({"message": f"Weather data for {city} created successfully"}), 201)

@app.route('/weather/<string:city>/', methods=['PUT'])
def update_weather_data(city):
    data = request.get_json()
    if not data or 'temperature' not in data or 'weather' not in data:
        return make_response(jsonify({"error": "Invalid data format"}), 400)

    if city not in weather_data:
        return make_response(jsonify({"error": "City not found"}), 404)

    weather_data[city]['temperature'] = data['temperature']
    weather_data[city]['weather'] = data['weather']
    return jsonify(weather_data[city])

@app.route('/weather/<string:city>/', methods=['DELETE'])
def delete_weather_data(city):
    if city not in weather_data:
        return make_response(jsonify({"error": "City not found"}), 404)

    del weather_data[city]
    return '', 204  # No content, successful deletion

if __name__ == "__main__":
    app.run()


# from flask import Flask, jsonify, make_response, request
# from weather_data import get_weather  # Import from the new module


# app = Flask(__name__)



# app = Flask(__name__)

# @app.route('/weather/<string:city>/')
# def get_weather_by_city(city):
#     weather_info = get_weather(city)
#     if weather_info:
#         return jsonify(weather_info),200
#     else:
#         return make_response(jsonify({"error": "City not found"}), 404)

# @app.route('/weather/add', methods=['POST'])
# def add_weather():
#     data = request.get_json()

#     if 'city' not in data or 'temperature' not in data or 'weather' not in data:
#         return make_response(jsonify({"error": "Missing data"}), 400)

#     city = data['city']
#     temperature = data['temperature']
#     weather = data['weather']

#     if get_weather(city):
#         return make_response(jsonify({"error": "City already exists"}), 400)

#     add_weather_data(city, temperature, weather)

#     return jsonify({"message": f"Weather data for {city} added successfully"})


# # Run the app if this script is the main program
# if __name__ == "__main__":
#     app.run()


# # Define a basic route that returns "Hello, World!"
# # @app.route("/")
# # def hello_world():
# #     return "Hello, World!"

# # Run the app if this script is the main program
# # if __name__ == "__main__":
# #     app.run()


# #
# #pip install Flask pytest Flask-Testing
# #python -m unittest test_weather.py