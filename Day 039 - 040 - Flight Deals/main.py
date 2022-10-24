from datetime import datetime
from data_manager import DataManager
from env import username, project, sheet, token
from flight_search import FlightSearch

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%I:%M:%S %p")
sheet_data = DataManager(username=username, project=project, sheet=sheet, token=token)

for i in range(0, len(sheet_data.prices)):
    code = sheet_data.prices[i]['iata']
    flight = FlightSearch(iataCode=code)
    parameters = {"price": {
        "lowest": flight.price
    }}
    sheet_data.put_data(object_id=sheet_data.prices[i]['id'], parameters=parameters)

print(sheet_data.prices)
