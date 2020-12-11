import requests
import json

with open('config.json', 'r') as f:
    json_file = json.load(f)
    keys = json_file["API-keys"]
    w_api_key = keys["weather"]
    city = json_file['city']


def weather_info() -> tuple:
    """
    returns a description of the sky and the temperature in celsius

    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city.lower()
    complete_url = base_url + "q=" + city_name + "&appid=" + w_api_key
    weather = requests.get(complete_url).json()
    if weather['cod'] != '404':
        s = weather['weather']
        sky = s[0]['description']
        t = weather['main']
        temperature = str(int(float(t['temp']) - 274.1))  # -274.1 converts kelvin to celsius
        max_temp = str(int(float(t['temp_max']) - 274.1))
        min_temp = str(int(float(t['temp_min']) - 274.1))
        return max_temp, min_temp, sky, temperature


a, b, skies, temp = weather_info()
weather_announcement = " Today's weather forecast:" + skies + ' skies, with a temperature of ' \
                       + temp + " degree celsius"
