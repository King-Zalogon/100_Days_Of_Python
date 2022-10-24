class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass

import requests
from datetime import datetime

SHEETY_USERNAME = ""
SHEETY_PROJECT_NAME = "myWorkouts"
SHEETY_SHEET_NAME = "workouts"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"
SHEETY_TOKEN = "Bearer 0c945xd54lir875sio740"

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%I:%M:%S %p")

sheety_header = {
    "Authorization": SHEETY_TOKEN
}

for param in today_workout:
    sheety_parameters = param
    sheety_post = requests.post(SHEETY_ENDPOINT, headers=sheety_header, json=sheety_parameters)
    sheety_post.raise_for_status()

# sheety_response = requests.get(SHEETY_ENDPOINT, headers=sheety_header)
# sheety_result_get = sheety_response.json()

print(sheety_result_post)