from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    # Prompt user to make a drink choice
    available_items = menu.get_items()
    user_choice = input(f"📤 What would you like? ({available_items}): ")
    # Turn off the Coffee Machine by entering “off” to the prompt.
    if user_choice == 'off':
        is_on = False
    # Print report.
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        # Searches the menu for a particular drink based on user choice
        drink = menu.find_drink(user_choice)
         # Check resources sufficient and process coins and check transaction successful
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # Make Coffee
            coffee_maker.make_coffee(drink)