from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu_item = MenuItem
menu = Menu()
is_on = True
#code starts here
while is_on:

    options = menu.get_items()
    choice = input(f"what would you like ? {options}:")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffeemaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffeemaker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
            else:
                is_on = False







