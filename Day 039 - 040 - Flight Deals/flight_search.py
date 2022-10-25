import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, **kwargs):
        self.iata_code = kwargs.get('iataCode')
        self.city = kwargs.get('city')
        self.apikey = kwargs.get('apikey')
        self.endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.header = {'apikey': self.apikey}
        self.parameters = {"term": self.city, "locations_types": "city"}
        self.response = None
        self.price = "TESTING"

    def code_search(self):
        self.response = requests.get(self.endpoint, headers=self.header, params=self.parameters)
        self.response.raise_for_status()
        result = self.response.json()
        return result['locations'][0]['code']
