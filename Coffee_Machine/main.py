MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": [500, 'ml'],
    "milk": [200, 'ml'],
    "coffee": [100, 'gr'],
    "funds": [100, "$"],
}

COIN_VALUES = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}

# For Emojis: During text entry, type Windows logo key  + . (period). The emoji keyboard will appear. 😀 ☕

# TODO: Keep track of the imported modules and __main__ variables

from IPython.display import clear_output
import time
from art_coffee import logo

# for i in range(3, 0, -1):
#     clear_output(wait=True)
#     print(i)
#     time.sleep(1)



# TODO: function for money input, checks against selection's price. Returns money if < price, or chance if > price


def money(coins_inserted):
    cash = 0
    for coin in coins_inserted:
        cash += COIN_VALUES[coin] * coins_inserted[coin]

    return cash


def charge(choice, payment):
    price = MENU[choice]["cost"]

    coins_inserted = {'quarters': 0, 'dimes': 0, 'nickles': 0, 'pennies': 0}

    print(f'The price of your {choice} is ${price}')
    print('Please specify amount of each coin inserted.')

    for coin in coins_inserted:
        try:
            coins_inserted[coin] = int(input(f'How many {coin} are you entering? '))

        except:
            print("That's not a valid amount. It will be taken as equal to '0'. We are sorry")
            coins_inserted[coin] = 0

        else:
            payment = money(coins_inserted)

    print(f"You've enter a total amount of ${payment}")

    if payment < price:
        print("Sorry that's not enough money. Money refunded.")
        cash = 0
        paid = False
    elif payment == price:
        print('Thanks. Your order will be ready soon.')
        resources['funds'][0] += price
        paid = True
    elif payment > price:
        print(f'Thanks, here is your change: {round((payment - price), 2)}. Your order will be ready soon')
        resources['funds'][0] += price
        paid = True
    else:
        print('Ooops, something went wrong with your payment')

    return paid


# TODO: Ask user for choice input: espresso, latte, capuccino


def user_choice():
    choices = ['espresso', 'latte', 'cappuccino', 'report', 'off']
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    checked = False

    while not checked:
        try:
            choices.index(choice)

        except KeyError:
            choice = input("That's not a valid option. Type 'espresso', 'latte' or 'cappuccino': ").lower()

        except:
            choice = input("That's not a valid option. Type 'espresso', 'latte' or 'cappuccino': ").lower()

        else:
            if choice == 'off':
                break

            elif choice == 'report':
                break
            else:
                print(f'You want a {choice}, great choice!')
                break

    return choice


# TODO: Define an "Off" function to break the loop when entered as user's choice


def turn_off(choice):
    if choice == 'off':
        print('Ok, night night!')
        return True


# TODO: Define a "Report" function


def report(choice, resources):

    if choice == 'report':
        print('Yes, master.\nHere is the current status:')
        for item in resources:
            if item == 'funds':
                print(f'{(item).capitalize()}: {resources[item][1]}{resources[item][0]}')
            else:
                print(f'{(item).capitalize()}: {resources[item][0]}{resources[item][1]}')


# TODO define a resource checking funct: choice's required resources VS current resources


def enough_resources(choice, resources):

    for resource in MENU[choice]["ingredients"]:
        needed = MENU[choice]["ingredients"][resource]
        current = resources[resource][0]
        if needed > current:
            print(f'Sorry, not enough {resource} for that option')
            return False
    return True


# TODO define a funct that adjust current resources after payment

def adjust_resources(choice, resources):

    for resource in MENU[choice]["ingredients"]:
        needed = MENU[choice]["ingredients"][resource]
        resources[resource][0] -= needed
        if resources[resource][0] == 0:
            print(f"We've just run out of {resource}.")
            print(f'But we had enough to make your {choice}.')


# TODO define the mother function that brings the other together

def coffee_machine():
    '''
    Main function for the coffee machine project.
    :return:
    '''

    machine_on = True

    print('Welcome to the Coffee Machine!')
    print(logo)

    while machine_on:
        choice = user_choice()

        if turn_off(choice):
            break

        report(choice, resources)

        if choice != 'report':
            paid = False
            payment = 0

            while not paid:
                if enough_resources(choice, resources):
                    paid = charge(choice, payment)
                    if paid:
                        for i in range(4):
                            loader = '.'
                            clear_output(wait=True)
                            print(loader*i)
                            time.sleep(1)

                        print('Payment successful. Please hold on, your order will be ready in: ')
                        adjust_resources(choice, resources)
                        for i in range(3, 0, -1):
                            clear_output(wait=True)
                            print(i)
                            time.sleep(1)
                        print(f'Here is your {choice}: ☕\nEnjoy!')
                        break
                    else:
                        print('Payment was not processed. Please choose again')
                        break
                else:
                    print('If not enough resources, please contact the admin')
                    break



coffee_machine()

