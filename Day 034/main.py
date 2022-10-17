# age : int
# name : str

# def  age_check(age: int):
#     if age >= 18:
#         print("Old enough")
#     else:
#         print('Too young to drive')

def age_check(age: int) -> bool:
    return age >= 18


print(age_check(11))
