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
    "water": [300, 'ml'],
    "milk": [200, 'ml'],
    "coffee": [100, 'gr'],
    "funds": [100, "$"],
}

# For Emojis: During text entry, type Windows logo key  + . (period). The emoji keyboard will appear. 😀 ☕

# TODO: Keep track of the imported modules and __main__ variables

machine_on = True

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

coins_value = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01} # I should change to COINS_VALUE

funds = 0
payment = 0

paid = False

# TODO: function for money input, checks against selection's price. Returns money if < price, or chance if > price


def money(coins_inserted):
    cash = 0
    for coin in coins_inserted:
        cash += coins_value[coin] * coins_inserted[coin]

    return cash


def charge(choice, payment):

    price = MENU[choice]["cost"]

    coins_inserted = {'quarters': 0, 'dimes': 0, 'nickles': 0, 'pennies': 0}

    print(f'The price of your {choice} is ${price}')
    print('Please specify amount of each coin inserted.')

    for coin in coins_inserted:
        try:
            coins_inserted[coin] = int(input(f'How many {coin} are you entering? '))
            payment = money(coins_inserted)

        except TypeError:
            coins_inserted[coin] = int(input(f"That's nota a valid option. Please enter your {coin} as numbers: "))

    if payment < price:
        print("Sorry that's not enough money. Money refunded.")
        cash = 0
    elif payment == price:
        print('Thanks. Your order will be ready soon.')
    elif payment > price:
        print(f'Thanks, here is your change: {payment - price}. Your order will be ready soon')
    else:
        print('Ooops, something went wrong with your payment')

    paid = True

    return paid


# TODO: Ask user for choice input: espresso, latte, capuccino


def user_choice():
    choices = ['espresso', 'latte', 'cappuccino', 'report', 'off']
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    checked = False

    while not checked:
        try:
            MENU[choice]

        except KeyError:
            choice = input("That's not a valid option. Type 'espresso', 'latte' or 'cappuccino': ").lower()

        else:
            if choice == 'off':
                turn_off((choice))
            elif choice == 'report':
                report(choice, resources)
            else:
                print(f'You want a {choice}, great choice!')
                return choice


# TODO: Define an "Off" function to break the loop when entered as user's choice


def turn_off(choice):
    if choice == 'off':
        print('Ok, night night!')
        return False


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