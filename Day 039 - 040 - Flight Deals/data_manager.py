import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.username = sheety_username
        self.project = sheety_project
        self.sheet = sheety_sheet
        self.endpoint = f"https://api.sheety.co/{self.username}/{self.project}/{self.sheet}"
        self.token = sheety_token
        self.header = {"Authorization": self.token}
        self.parameters = sheety_parameters
        self.get_response = None
        self.post_response = None

        self.get_result = self.get_data()
        self.post_result = self.post_data()

    def get_data(self):
        self.get_response = requests.get(self.endpoint, headers=self.header)
        self.get_response.raise_for_status()
        return self.get_response.json()

    def post_data(self):
        self.post_response = requests.post(self.endpoint, headers=self.header, json=self.parameters)
        self.post_response.raise_for_status()
        return self.post_response.json()
