import requests

MY_LAT = -34.603683
MY_LNG = -58.381557
MY_POSS = (MY_LNG, MY_LAT)

parameters = {
    'appid': "22b4fd0b83c519a0dbd9f95b66103ee8",
    'lat': MY_LAT,
    'lon': MY_LNG,
    'units': "metric"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)

data = response.json()

print(data)

