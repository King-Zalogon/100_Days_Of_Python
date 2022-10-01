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

# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])
# print(type(data))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)
#
# print(data['temp'].mean())
#
# print(data['temp'].max())
# print(data['condition'])
# print(data.condition)
#
# print(data[data.temp == data.temp.max()])
#
# monday = (data[data.day == 'Monday']).temp * 9/5 + 32
# print(monday)

data_dict = {
    'students': ['Any', 'James', 'Angela'],
    'scores': [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')
