from platform import machine


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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_balance = 0


def get_order():
    order = "nothing"
    available_options = ('espresso', 'latte', 'cappuccino', 'off', 'report')
    while not order in available_options:
        order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == 'off':
        exit()
    elif order == 'report':
        print_report()
    else:
        drink = MENU[order]
        if check_resources(drink):
            payment = get_payment()
            if (MENU[order]["cost"] <= payment):
                make_coffee(order, payment)
            else:
                print("Sorry that's not enough money. Money refunded.")
    get_order()


def print_report():
    print(f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${machine_balance}""")


def check_resources(drink):
    for ingredient in drink['ingredients']:
        if (drink['ingredients'][ingredient] > resources[ingredient]):
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def make_coffee(order, payment):
    for ingredient in MENU[order]['ingredients']:
        resources[ingredient] -= MENU[order]['ingredients'][ingredient]
    global machine_balance
    machine_balance += MENU[order]['cost']

    give_change(MENU[order]['cost'], payment)


def get_payment():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = sum((quarters * 0.25, dimes * 0.1, nickles * 0.05, pennies * 0.01))
    return total


def give_change(cost, payment):
    change = round(payment - cost, 2)
    print(f"Here is ${change} in change.")


get_order()
