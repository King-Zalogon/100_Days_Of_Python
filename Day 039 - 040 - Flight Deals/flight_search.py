class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, **kwargs):
        self.iata_code = kwargs.get('iataCode')
        self.price = "TESTING"

    def code_search(self, **kwargs):
        pass
