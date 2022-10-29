import datetime
from data_manager import DataManager
from env import username, project, sheet, token, apikey
from flight_search import FlightSearch
from flight_data import FlightData

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

date = datetime.datetime.now().strftime("%d/%m/%Y")
today = datetime.datetime.now()
time = datetime.datetime.now().strftime("%I:%M:%S %p")
tomorrow = (today + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
min_return_date = (today + datetime.timedelta(days=7)).strftime("%d/%m/%Y")
max_depart_date = (today + datetime.timedelta(days=23)).strftime("%d/%m/%Y")
max_return_date = (today + datetime.timedelta(days=30)).strftime("%d/%m/%Y")

sheet_data = DataManager(username=username, project=project, sheet=sheet, token=token)

# for i in range(0, len(sheet_data.prices)):
#     city = sheet_data.prices[i]['city']
#     flight = FlightSearch(city=city, apikey=apikey)
#     search = flight.flight_search()
#     if len(search["data"]) != 0:
#         price = search["data"][0]["price"]
#         print(f"{city}: ${price}")
#         parameters = {"price": {
#             "iata": flight.code_search(),
#             "lowest": price
#         }}
#         sheet_data.put_data(object_id=sheet_data.prices[i]['id'], parameters=parameters)
#     else:
#         print(f"No option was found for {city}")

print(sheet_data.prices)

for trip in sheet_data.prices:
    if trip['lowest'] is str:
        if trip['lowest'] <= trip['target']:
            print(f"Low price found! Trip for {trip['city']} only u$d{trip['lowest']}!")
        else:
            print(f"No good prices for {trip['city']}.")
    else:
        print(f"No flight found for {trip['city']}")
