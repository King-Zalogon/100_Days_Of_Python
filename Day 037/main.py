import os
import requests
from _datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

PIXELA_URL = "https://pixe.la/v1/users"
USER_NAME = os.getenv('USER')
TOKEN = os.getenv('TOKEN')
GRAPH_ID = "graph1"
TODAY = dt.now().strftime("%Y%m%d")

# TODO Create a user account - DONE

user_parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_URL, json=user_parameters)
# print(response.text)

# response was: {"message":"Success. Let's visit https://pixe.la/@zalogon , it is your profile page!","isSuccess":true}
# {"message":"Success. Let's visit https://pixe.la/@zalogonkin , it is your profile page!","isSuccess":true}
# {"message":"Success. Let's visit https://pixe.la/@zalogonking , it is your profile page!","isSuccess":true}
# {"message":"Specified graphID not exist.","isSuccess":false}

# TODO Create a graph definition

# user_parameters = {
#     "token": TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

graph_endpoint = f"{PIXELA_URL}/{USER_NAME}/graphs"

# graph_config = {
#     "id": GRAPH_ID,
#     "name": "PushUps",
#     "unit": "Push",
#     "type": "int",
#     "color": "momiji",
#     }

# headers = {
#     "X-USER-TOKEN": TOKEN
#     }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# TODO View the graph

graph_view = f'https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}'

# TODO Posting value into the graph

pixel_data = {
    "name" : "PushUps",
    "date": TODAY,
    "quantity": "50",

    }

headers = {
    "X-USER-TOKEN": TOKEN
    }

pixel_creation_endpoint = f"{PIXELA_URL}/{USER_NAME}/graphs/{GRAPH_ID}"
Could add /{YYYYMMDD} to the end point to update a pixel

# response = requests.put(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# TODO Update a pixel

# update_endpoint = f"{PIXELA_URL}/{USER_NAME}/graphs/{GRAPH_ID}/20221021"
# pixel_data = {
#     "name" : "PushUps",
#     "date": "20221020",
#     "quantity": "500",
# }
#
# response = requests.put(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# TODO Delete a pixel

# delete_pixel_endpoint = f"{PIXELA_URL}/{USER_NAME}/graphs/{GRAPH_ID}/20221020"
# delete_pixel_data = {
#
# }
#
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
