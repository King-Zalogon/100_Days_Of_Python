import requests
from _datetime import datetime as dt

PIXELA_URL = "https://pixe.la/v1/users"
USER_NAME = ""
TOKEN = ""
GRAPH_ID = "graph1"
TODAY = dt.now().strftime("%Y%m%d")

# TODO Create a user account - DONE
# user_parameters = {
#     "token": "Not a token",
#     "username": "zalogon",
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=PIXELA_URL, json=user_parameters)
# print(response.text)
# response was: {"message":"Success. Let's visit https://pixe.la/@zalogon , it is your profile page!","isSuccess":true}

# TODO Create a graph definition

# user_parameters = {
#     "token": TOKEN,
#     "username": USER_NAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
#
# graph_endpoint = f"{PIXELA_URL}/{USER_NAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "PushUps",
#     "unit": "Pushes",
#     "type": "int",
#     "color": "momiji",
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# TODO View the graph

graph_view = "https://pixe.la/v1/users/zalogon/graphs/graph1"

# TODO Posting value into the graph

# pixel_data = {
#     "name" : "PushUps",
#     "date": TODAY,
#     "quantity": "50",
#
# }

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{PIXELA_URL}/{USER_NAME}/graphs/{GRAPH_ID}"
# Could add /{YYYYMMDD} to the end point to update a pixel

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

delete_pixel_endpoint = f"{PIXELA_URL}/{USER_NAME}/graphs/{GRAPH_ID}/20221020"
delete_pixel_data = {

}

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)