# old_list = [1, 2, 3]
# new_list = []
# for n in old_list:
#     add_n = n + 1
#     new_list.append(add_n)
#
# print(new_list)

# new_list = [n + 1 for n in old_list]
# print(new_list)

# with open('file1.txt') as list1:
#     list_1 = [int(item[0:-1]) for item in list1.readlines()]
#     print(list_1)
#
# with open('file2.txt') as list2:
#     list_2 = [int(item[0:-1]) for item in list2.readlines()]
#
# result = list(set(list_1).intersection(set(list_2)))

# with open('file1.txt') as list1:
#     list_1 = list1.readlines()
# with open('file2.txt') as list2:
#     list_2 = list2.readlines()
# result = [int(num) for num in list_1 if num in list_2]

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = { word : len(word) for word in sentence.split(' ')}

# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
#
# weather_f = {key: (int(value * 9/5) + 32) for (key, value) in weather_c.items()}
#
# print(weather_f)

# import random
# import pandas
# names = ['Angus', 'Luis', 'Palo', 'Yosho', 'Ken']
#
# students_scores = {student: random.randint(1, 10) for student in names}
#
# passed_students = {key: value for (key, value) in students_scores.items() if value >= 6}
#
# students_dict = {"student":['Angus', 'Luis', 'Palo', 'Yosho', 'Ken'], "score":[6, 5, 8, 8, 2]}
#
# student_data_frame = pandas.DataFrame(students_dict)
# print(student_data_frame)

# Looping through Data Frames

# for (key, value) in student_data_frame.items():
#     print(key)
#     print(value)

# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)
#     if row.score > 5:
#         print('Passed')
#     else:
#         print('Failed')
