import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = "70"
HEIGHT_CM = "177"
AGE = "33"

os.environ["APP_ID"] = ""
os.environ["API_KEY"] = ""
print(os.environ)
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_USERNAME = ""
SHEETY_PROJECT_NAME = "myWorkouts"
SHEETY_SHEET_NAME = "workouts"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{SHEETY_PROJECT_NAME}/{SHEETY_SHEET_NAME}"
SHEETY_TOKEN = "Bearer 0c945xd54lir875sio740"

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%I:%M:%S %p")

# NUTRITIONIX request(.post) and response:

exercise_text = input("Which exercises did you complete today? ")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # "x-remote-user-id": "",
    # "x-user-jwt": "",
}

nutritionix_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutritionix_response = requests.post(NUTRITIONIX_ENDPOINT, json=nutritionix_parameters, headers=nutritionix_headers)
nutritionix_response.raise_for_status()
nutritionix_result = nutritionix_response.json()
print(nutritionix_result)

# result_example = {'exercises': [
#     {'tag_id': 317, 'user_input': 'ran', 'duration_min': 24.86, 'met': 9.8, 'nf_calories': 259.87,
#      'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg',
#                'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False},
#      'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None},
#     {'tag_id': 763, 'user_input': 'abs', 'duration_min': 10, 'met': 2.8, 'nf_calories': 29.87, 'photo':
#         {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/763_highres.jpg',
#          'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/763_thumb.jpg', 'is_user_uploaded': False},
#      'compendium_code': 2024, 'name': 'sit-ups', 'description': None, 'benefits': None}
# ]
# }

today_workout=[]

for exercise in nutritionix_result['exercises']:
    today_workout.append({"workout": {
                           "date": date,
                           "time": time,
                           "exercise": exercise["name"].capitalize(),
                           "duration": exercise["duration_min"],
                           "calories": exercise["nf_calories"]
            }
        }
    )

print(today_workout)

# Sheety get and post:

sheety_header = {
    "Authorization": SHEETY_TOKEN
}

for param in today_workout:
    sheety_parameters = param
    sheety_post = requests.post(SHEETY_ENDPOINT, headers=sheety_header, json=sheety_parameters)
    sheety_post.raise_for_status()
    # sheety_result_post = sheety_post.json()
    # print(sheety_result_post)

# sheety_response = requests.get(SHEETY_ENDPOINT, headers=sheety_header)
# sheety_result_get = sheety_response.json()

# print(sheety_result_post)


