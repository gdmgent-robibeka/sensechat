import pyowm

def get_current_weather():
    owm = pyowm.OWM('f12ef8a8dc87e23556868b9967690c88')
    observation = owm.weather_at_place("Gent, BE")
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    return str(round(temperature))
