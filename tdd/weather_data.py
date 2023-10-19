# weather_data.py

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}

def get_weather(city):
    return weather_data.get(city, None)

# Endpoint      Methods  Rule
# -----------  -------  ------------------------
# create_weather_data    POST    /weather/
# delete_weather_data    DELETE  /weather/<string:city>/
# get_weather_by_city    GET     /weather/<string:city>/
# update_weather_data    PUT     /weather/<string:city>/
