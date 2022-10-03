# # with open('weather_data.csv') as file:
# #     data = file.readlines()
# #
# # print(data)
#
# # import csv
#
# # with open('weather_data.csv') as file:
# #     data = csv.reader(file)
# #     temperature = []
# #     for row in data:
# #         temperature.append(row[1])
# #     temperature.remove('temp')
# #     for i in range(len(temperature)):
# #         temperature[i] = int(temperature[i])
# #     print(temperature)
#
# import pandas
#
# # data = pandas.read_csv('weather_data.csv')
# # print(data['temp'])
# # print(type(data))
# #
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data['temp'].to_list()
# # print(temp_list)
# #
# # avg_temp = sum(temp_list)/len(temp_list)
# # print(avg_temp)
# #
# # print(data['temp'].mean())
# #
# # print(data['temp'].max())
# # print(data['condition'])
# # print(data.condition)
# #
# # print(data[data.temp == data.temp.max()])
# #
# # monday = (data[data.day == 'Monday']).temp * 9/5 + 32
# # print(monday)
#
# data_dict = {
#     'students': ['Any', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')
import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

dict = data.to_dict()

fur_color_count = data['Primary Fur Color'].value_counts()

print(fur_color_count)

grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
