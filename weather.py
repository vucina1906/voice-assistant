import requests
from apikeys import weather_key

api_address = 'http://api.openweathermap.org/data/2.5/weather?q=Belgrade&appid='+weather_key 
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data['main']['temp']-273,1)
    return temperature

def des():
    description=json_data["weather"][0]['description']
    return description

