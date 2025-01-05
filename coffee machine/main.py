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

def resource_sufficient(res):
    """returns resource availability"""
    for items in res:
        if res[items] >= resources[items]:
            print(f"Sorry there is not enough {items}.")
            return False
    else:
            return True

def calculate_money():
    """returns total values"""
    total = 0
    print("enter the coins")
    total += int(input("Enter the number of quarters"))*0.25
    total += int(input("Enter the number of dimes"))*0.1
    total += int(input("Enter the number of nickel"))*0.05
    total += int(input("Enter the number of pennies"))*0.01
    return total
def enough_money(money_r,total_money):
    """USED TO CHECK IF CORRECT AMOUNT OF MONEY IS RECIEVED"""
    global profit
    if money_r>=total_money:
        change = round(money_r-total_money,2)
        profit += total_money

        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
def make_coffee(drinkname,order_ingredients):
    global resources
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Your coffee {drinkname} is made")


#todo 1: . Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
profit = 0
is_continue = True
while is_continue:
  choice = input(print("What would you like? (espresso/latte/cappuccino):"))
  if choice=="off":
      is_continue = False
  elif choice=="record":
      print(f"water:{resources['water']} ml")
      print(f"milk:{resources['milk']} ml")
      print(f"coffee:{resources['coffee']} g")
      print(f"cash:${profit}")
  else:
      coffee = MENU[choice]
      if resource_sufficient(coffee["ingredients"]):
        get_money = calculate_money()
        if enough_money(get_money,coffee["cost"]):
            make_coffee(choice,coffee["ingredients"])



