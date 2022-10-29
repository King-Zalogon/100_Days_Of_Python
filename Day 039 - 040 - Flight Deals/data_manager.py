import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, **kwargs):
        self.username = kwargs.get("username")
        self.project = kwargs.get("project")
        self.sheet = kwargs.get("sheet")
        self.endpoint = f"https://api.sheety.co/{self.username}/{self.project}/{self.sheet}"
        self.token = kwargs.get("token")
        self.header = {"Authorization": self.token}
        # self.parameters = kwargs.get("parameters")
        self.get_response = None
        self.post_response = None
        self.put_response = None
        self.object_id = None

        self.get_result = self.get_data()
        self.prices = self.get_result["prices"]

    def get_data(self):
        self.get_response = requests.get(self.endpoint, headers=self.header)
        self.get_response.raise_for_status()
        return self.get_response.json()

    def post_data(self, **kwargs):
        self.post_response = requests.post(self.endpoint, headers=self.header, json=kwargs.get("parameters"))
        self.post_response.raise_for_status()
        return self.post_response.json()

    def put_data(self, **kwargs):
        self.object_id = kwargs.get("object_id")
        self.endpoint = f"https://api.sheety.co/{self.username}/{self.project}/{self.sheet}/{self.object_id}"
        self.put_response = requests.put(self.endpoint, headers=self.header, json=kwargs.get("parameters"))
        return self.put_response.json()
