from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = CoffeeMaker()
MENU = Menu()
Money_machine = MoneyMachine()
machine_is_on = True

while machine_is_on:
    choice = input(f"What would you like? {(MENU.get_items())}: ").lower()
    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        make_coffee.report()
        Money_machine.report()
    elif MENU.find_drink(choice):
        drink = MENU.find_drink(choice)
        if make_coffee.is_resource_sufficient(drink) and Money_machine.make_payment(drink.cost):
            make_coffee.make_coffee(drink)








