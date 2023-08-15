import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# CONSTANTS AND ENVIRO VARS
GENDER = os.getenv('GEN')
WEIGHT_KG = os.getenv('WEIGHT')
HEIGHT_CM = os.getenv('HEIGHT')
AGE = os.getenv('AGE')

APP_ID = os.getenv('NUTRITIONIX_ID')
API_KEY = os.getenv('NUTRITIONIX_KEY')
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_USERNAME = os.getenv('SHEETY_USER')
SHEETY_PROJECT_NAME = "exerciseTracker"
SHEETY_SHEET_NAME = "exercises"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"
SHEETY_TOKEN = os.getenv('SHEETY_TKN')
BASIC_HEADER = os.getenv('SHEETY_BASIC')

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%I:%M:%S %p")

# NUTRITIONIX request(.post) and response:

exercise_text = input("Which exercises did you complete today? ")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY  # , "x-remote-user-id": "1"
}

nutritionix_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutritionix_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=nutritionix_parameters, headers=nutritionix_headers)
nutritionix_response.raise_for_status()
nutritionix_result = nutritionix_response.json()
# print(nutritionix_result)

today_workout = []

for exercise in nutritionix_result['exercises']:
    today_workout.append({'exercise': {
                           'date': date,
                           'time': time,
                           'exercise': exercise['name'].capitalize(),
                           'duration': exercise['duration_min'],
                           'calories': exercise['nf_calories']
            }
        }
    )


# Sheety get and post:

sheety_header = {"Authorization": f"Basic {BASIC_HEADER}="}

for param in today_workout:
    row_data = param
    response = requests.post(SHEETY_ENDPOINT, json=row_data, headers=sheety_header)
    print(response.text)


sheety_response = requests.get(SHEETY_ENDPOINT, headers=sheety_header)
sheety_result_get = sheety_response.json()

print(sheety_result_get)
