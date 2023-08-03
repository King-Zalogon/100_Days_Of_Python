import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Twilio Data
SID = os.getenv('TWI_ACC_SID')
AUTH_TOKEN = os.getenv('TWI_AUTH_TOKEN')
TWILIO_PHONE = os.getenv('RECEIVER_NUMBER')
MY_PHONE = os.getenv('FROM_NUMBER')


# Weather Data
API_KEY = os.getenv('WEATHER_KEY')
CITY_ID = 3433955
CURRENT_WEATHER_URL = f'https://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}'

parameters = {
    'id': CITY_ID,
    'appid': API_KEY,
}

response = requests.get(url=CURRENT_WEATHER_URL, params=parameters)
response.raise_for_status()
data = response.json()


condition = data['weather'][0]['description']
city = data['name']
temp = int(data['main']['temp']-273.15) # This rounds down, not accurate, but works for my tests
feels_like = int(data['main']['feels_like']-273.15)

weather_msg = f"In {city} the current temperature is {temp}°C with {condition} and it feels like it's {feels_like}°C."

client = Client(SID, AUTH_TOKEN)

message = client.messages.create(
    from_=TWILIO_PHONE,
    body=weather_msg,
    to=MY_PHONE
)

print(weather_msg)

