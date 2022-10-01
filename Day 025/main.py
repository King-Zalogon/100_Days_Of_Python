# with open('weather_data.csv') as file:
#     data = file.readlines()
#
# print(data)

# import csv

# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
#     temperature.remove('temp')
#     for i in range(len(temperature)):
#         temperature[i] = int(temperature[i])
#     print(temperature)

import pandas

data = pandas.read_csv('weather_data.csv')
print(data['temp'])
