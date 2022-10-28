class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight):
        self.flight_data = flight
        self.price = self.flight_data["data"][0]["price"]
        self.city_from = self.flight_data["data"][0]['cityCodeFrom']
        self.city_to = self.flight_data["data"][0]['cityCodeTo']
        self.fly_from = self.flight_data["data"][0]['flyFrom']
        self.fly_to = self.flight_data["data"][0]['flyTo']

        self.from_depart_date = self.flight_data["data"][0]['route'][0]['local_departure'].split("T")[0]
        self.from_depart_time = self.flight_data["data"][0]['route'][0]['local_departure'].split("T")[1].split(".")[0]

        self.to_arrive_date = self.flight_data["data"][0]['route'][0]['local_arrival'].split("T")[0]
        self.to_arrive_time = self.flight_data["data"][0]['route'][0]['local_arrival'].split("T")[1].split(".")[0]

        self.to_depart_date = self.flight_data["data"][0]['route'][1]['local_departure'].split("T")[0]
        self.to_depart_time = self.flight_data["data"][0]['route'][1]['local_departure'].split("T")[1].split(".")[0]

        self.from_arrive_date = self.flight_data["data"][0]['route'][1]['local_arrival'].split("T")[0]
        self.from_arrive_time = self.flight_data["data"][0]['route'][1]['local_arrival'].split("T")[1].split(".")[0]
