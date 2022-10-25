import requests
from env import username, project, sheet, token, apikey


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, **kwargs):
        self.iata_code = kwargs.get('iataCode')
        self.city = kwargs.get('city')
        self.apikey = kwargs.get('apikey')
        self.endpoint = "https://api.tequila.kiwi.com/"
        self.header = {'apikey': self.apikey}
        self.code_parameters = {"term": self.city, "locations_types": "city"}
        self.response = None
        self.price = None
        self.loc_query_endpoint_add_hoc = "locations/query"
        self.flight_search_endpoint_add_hoc = "v2/search"
        self.fly_from = "MIA"
        self.fly_to = self.code_search()
        self.dateFrom = "01/11/2022"  # dd/mm/yyyy
        self.dateTo = "30/11/2022"  # earch flights upto this date (dd/mm/yyyy)
        self.return_from = "1/12/2022"  # min return date of the whole trip (dd/mm/yyyy)
        self.return_to = "31/12/2022"
        self.flight_type = "round"
        self.one_for_city = 1
        self.adults = 1
        self.adult_hold_bag = "1"
        self.adult_hand_bag = "1"
        self.partner_market = "us"
        self.curr = "USD"
        self.price_from = "50"
        self.price_to = "10000"
        self.max_stopovers = 1
        self.flight_parameters = {"fly_from": self.fly_from,
                                  "fly_to": self.fly_to,
                                  "dateFrom": self.dateFrom,
                                  "dateTo": self.dateTo,
                                  "return_from": self.return_from,
                                  "return_to": self.return_to,
                                  "flight_type": self.flight_type,
                                  "one_for_city": self.one_for_city,
                                  "adults": self.adults,
                                  "adult_hold_bag": self.adult_hold_bag,
                                  "adult_hand_bag": self.adult_hand_bag,
                                  "partner_market": self.partner_market,
                                  "curr": self.curr,
                                  "price_from": self.price_from,
                                  "price_to": self.price_to,
                                  "max_stopovers": self.max_stopovers
                                  }

    def code_search(self):
        self.response = requests.get(f"{self.endpoint}{self.loc_query_endpoint_add_hoc}",
                                     headers=self.header, params=self.code_parameters)
        self.response.raise_for_status()
        code_result = self.response.json()
        return code_result['locations'][0]['code']

    def flight_search(self):
        self.iata_code = self.code_search()
        self.response = requests.get(f'{self.endpoint}{self.flight_search_endpoint_add_hoc}',
                                     headers=self.header, params=self.flight_parameters)
        self.response.raise_for_status()
        flight_result = self.response.json()
        return flight_result


flight = FlightSearch(apikey=apikey, city="New York")
print(flight.flight_search())