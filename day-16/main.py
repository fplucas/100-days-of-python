from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


def new_order():
    order = 'nothing'
    while order not in ('off', 'report', 'espresso', 'latte', 'cappuccino'):
        order = input(f"What would you like? ({menu.get_items()}): ")
    if order == 'off':
        exit()
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if (coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)
    new_order()


new_order()
