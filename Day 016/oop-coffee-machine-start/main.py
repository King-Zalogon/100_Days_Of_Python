from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "milk": 0,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
#
# resources = {
#     "water": [300, 'ml'],
#     "milk": [200, 'ml'],
#     "coffee": [100, 'gr'],
#     "funds": [100, "$"],
# }
#
# espresso = MenuItem('espresso', MENU['espresso']['ingredients']['water'], MENU['espresso']['ingredients']['milk'],
#                     MENU['espresso']['ingredients']['coffee'], MENU['espresso']['cost'])
#
# latte = MenuItem('latte', MENU['latte']['ingredients']['water'], MENU['latte']['ingredients']['milk'],
#                  MENU['latte']['ingredients']['coffee'], MENU['latte']['cost'])
#
# cappuccino = MenuItem('cappuccino', MENU['cappuccino']['ingredients']['water'],
#                       MENU['cappuccino']['ingredients']['milk'], MENU['cappuccino']['ingredients']['coffee'],
#                       MENU['cappuccino']['cost'])

menu = Menu()
c_maker = CoffeeMaker()
money_m = MoneyMachine()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? ({options}: ')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        c_maker.report()
        money_m.report()
    else:
        drink = menu.find_drink(choice)
        if c_maker.is_resource_sufficient((drink)) and money_m.make_payment(drink.cost):
            c_maker.make_coffee(drink)


# def user_choice():
#     choices = ['espresso', 'latte', 'cappuccino', 'report', 'off']
#     choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
#
#     checked = False
#
#     while not checked:
#         try:
#             choices.index(choice)
#
#         except KeyError:
#             choice = input("That's not a valid option. Type 'espresso', 'latte' or 'cappuccino': ").lower()
#
#         except:
#             choice = input("That's not a valid option. Type 'espresso', 'latte' or 'cappuccino': ").lower()
#
#         else:
#             if choice == 'off':
#                 break
#
#             elif choice == 'report':
#                 break
#             else:
#                 print(f'You want a {choice}, great choice!')
#                 break
#
#     return choice
#
#
# def money(coins_inserted):
#     cash = 0
#     for coin in coins_inserted:
#         cash += COIN_VALUES[coin] * coins_inserted[coin]
#
#     return cash
#
#
# def turn_off(choice):
#     if choice == 'off':
#         print('Ok, night night!')
#         return True


