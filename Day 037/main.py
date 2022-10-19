import requests

PIXELA_URL = "https://pixe.la/v1/users"

# TODO Create a user account - DONE
user_parameters = {
    "token": "NOT A TOKEN",
    "username": "zalogon",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_URL, json=user_parameters)
# print(response.text)
# response was: {"message":"Success. Let's visit https://pixe.la/@zalogon , it is your profile page!","isSuccess":true}

# TODO Create a graph definition
