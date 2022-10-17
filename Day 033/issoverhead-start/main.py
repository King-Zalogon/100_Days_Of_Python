import time

import requests
import datetime as dt
import smtplib

MY_LAT = -34.603683
MY_LNG = -58.381557
MY_POSS = (MY_LNG, MY_LAT)
MY_EMAIL = "zalogonking@gmail.com"
PASSWORD = 'udorlnhzwqvykhxv'


def is_night(sunrise_hour, sunset_hour, current_hour):
    """
    Used to determine if it's currently night according to the hour
    :param sunrise_hour: int with the hour of sunrise, 24-hour format.
    :param sunset_hour: int with the hour of sunset, 24-hour format.
    :param current_hour: int with current hour, 24-hour format.
    :return: boolean, True if current hour is between sunset and sunrise.
    """
    return not sunrise_hour < current_hour < sunset_hour


def relative_position(position_a, position_b):
    """
    Takes 2 tuples, each with longitude and latitude
    and checks if the differences between each tuple is less than 5 degrees for each, lat and long
    If so, returns true
    :param position_a: a tuple made of longitude in index 0 and latitude in 1
    :param position_b: a tuple made of longitude in index 0 and latitude in 1
    :return: a boolean, True if less than 5 degrees of latitude and longitude
    """
    long_check = position_a[0] - position_b[0]
    lat_check = position_a[1] - position_b[1]
    is_near = abs(long_check) < 5 and abs(lat_check) < 5
    return is_near


def conditions_check(condition_1, condition_2):
    check = condition_1 and condition_2
    return check


response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_data = response.json()
longitude = float(iss_data['iss_position']['longitude'])
latitude = float(iss_data['iss_position']['latitude'])
iss_position = (longitude, latitude)

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}
night_check = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}")
night_check.raise_for_status()  # It asks requests to raise the exception for me if an error occurs
night_data = night_check.json()

sunrise = int(night_data["results"]["sunrise"].split('T')[1].split(':')[0])
sunset = int(night_data["results"]["sunset"].split('T')[1].split(':')[0])

now = dt.datetime.now()
current_time = now.hour

# If the ISS is close to my current position
position = relative_position(MY_POSS, iss_position)


# and it is currently dark
night = is_night(sunrise, sunset, current_time)


# Then, send email to tell me to look up.
good_to_go = conditions_check(position, night)

while night:
    time.sleep(60)
    if good_to_go:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # to connect to de smtp of our mail
            connection.starttls()  # to encrypt the messages
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f'Subject: ISS is in the sky!\n\nCheck the sky, the International Space '
                                    f'Station should be passing through.')


# BONUS: run the code every 60 seconds.
