class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight):
        self.flight_data = flight
        self.price = self.flight_data["data"][0]["price"]
        self.city_from = self.flight_data["data"][0]['cityCodeFrom']
        self.city_to = self.flight_data["data"][0]['cityCodeTo']
        self.fly_from = self.flight_data["data"][0]['flyFrom']
        self.fly_to = self.flight_data["data"][0]['flyTo']
        self.depart_time = self.flight_data["data"][0]['route'][0]['local_departure']
        self.destination_arrive_time = self.flight_data["data"][0]['route'][0]['local_arrival']
        self.destination_depart_time = self.flight_data["data"][0]['route'][1]['local_departure']
        self.arrive_time = self.flight_data["data"][0]['route'][1]['local_arrival']



    pass
