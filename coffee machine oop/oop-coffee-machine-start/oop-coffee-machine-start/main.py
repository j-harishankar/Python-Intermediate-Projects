from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



is_continue = True
staff = CoffeeMaker()
customer_order = Menu()
profit = MoneyMachine()
while is_continue:
    x  = input(f"enter the coffee you want {customer_order.get_items()}")
    drinks = customer_order.find_drink(x)
    if x=='report':
        print(staff.report(),end='')
        print(profit.report())
    elif x=='off':
        is_continue=False
        print("The coffee machine has gone into power off mode")
    else:
        resource_available = staff.is_resource_sufficient(drinks)
        if resource_available:
            if profit.make_payment(drinks.cost):
                staff.make_coffee(drinks)
            else:
                print("Not enough money your cash has been refunded...")
        else:
            print(f"resource not available to make {drinks.name}")


