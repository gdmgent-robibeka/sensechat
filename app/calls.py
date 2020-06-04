import pyowm
import requests

def get_current_weather():
    owm = pyowm.OWM('f12ef8a8dc87e23556868b9967690c88')
    observation = owm.weather_at_place("Gent, BE")
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    return str(round(temperature))

def get_cat_fact():
    response = requests.get("https://meowfacts.herokuapp.com/")
    response = response.json()['data']
    fact = ''.join(map(str, response))
    return fact