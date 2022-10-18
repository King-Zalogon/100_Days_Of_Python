import requests

from twilio.rest import Client

account_sid = ""
auth_token = ""

TWILIO_PHONE = ""
MY_PHONE = ""

MY_LAT = -34.603683
MY_LNG = -58.381557
MY_POSS = (MY_LNG, MY_LAT)
CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
ONE_CALL_URL = "https://api.openweathermap.org/data/2.5/onecall"
HOURLY_URL = "https://pro.openweathermap.org/data/2.5/forecast/hourly"
ANGELA_KEY = ""
API_KEY = ""

parameters = {
    'appid': "",
    'lat': MY_LAT,
    'lon': MY_LNG,
    'units': "metric",
    "exclude": ["currently", "minutely", "daily"],
}

response = requests.get(url=ONE_CALL_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()

# for i in range(0, 12):
#     if weather_data['hourly'][i]['weather'][0]['id'] < 700:
#         print(f'Umbrella needed {i+1} hours from now.')
#         print(f"Some {weather_data['hourly'][i]['weather'][0]['description']} in the forecast {i+1} hours from now.")

will_rain = False
weather_msg = "Nothing to report, master"
weather_slice = weather_data["hourly"][:12]

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    print(weather_data['hourly'].index(hour_data))
    if condition_code < 700:
        will_rain = True
        weather_msg = f"Some {weather_data['hourly'][weather_data['hourly'].index(hour_data)]['weather'][0]['description']} in the forecast {(weather_data['hourly'].index(hour_data))+1} hours from now."

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body= weather_msg,
        from_= TWILIO_PHONE,
        to= MY_PHONE
    )

    print(message.status)
