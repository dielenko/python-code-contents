############### Coffee Machine Project #####################
from replit import clear
from coffee_machine_data import MENU, resources
from art import logo

# Create function which modifying Global Scope for machine_resources{}.
def increase_resources(machine_resources_input):
    """Modifying Global Scope for machine_resources{}."""
    machine_resources = machine_resources_input
    return machine_resources

# Create function which check the user’s input to decide what to do next.
def check_input(user_input):
    """Check the user's input to decide what to do next."""
    # For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
    # When the user enters “report” to the prompt, a report should be generated that shows the current resource values. e.g.
    if user_input == 'espresso':
        return 'espresso'
    elif user_input == 'latte':
        return 'latte'
    elif user_input == 'cappuccino':
        return 'cappuccino'
    elif user_input == 'off':
        return 'turn_off'
    else:
        return 'report'

# Create function which print report of coffee machine resources.
def print_report(current_machine_resources, money_input):
    """Print report of coffee machine resources."""
    report_resources = {}
    for key, value in current_machine_resources.items():
        if key == 'coffee':
            unit = 'g'
        else:
            unit = 'ml'
        report_resources[key]= (f"{value}{unit}")
    report_resources["money"]= (f"${money_input}")
    return report_resources

# Create function which check machine resources sufficient.
def check_resources_sufficient(order_input, origin_machine_resources):
    """Check machine resources sufficient."""
    milk_included = False
    # When the user chooses a drink, the program should check if there are enough resources to make that drink.
    # Define ingredients to provision the user order.
    order_ingredient_water = MENU[order_input]["ingredients"]['water']
    order_ingredient_coffee = MENU[order_input]["ingredients"]['coffee']
    if order_input == 'latte' or order_input == 'cappuccino':
        milk_included = True
        order_ingredient_milk = MENU[order_input]["ingredients"]['milk']
    # Define origin ingredient resources prior the last user order.
    origin_ingredient_water = origin_machine_resources['water']
    origin_ingredient_coffee = origin_machine_resources['coffee']
    origin_ingredient_milk = origin_machine_resources['milk']
    # Check if there are enough resources to make that drink.
    if order_ingredient_water > origin_ingredient_water:
        return '😯 Sorry there is not enough water!'
    if order_ingredient_coffee > origin_ingredient_coffee:
        return '😯 Sorry there is not enough coffee!'
    if milk_included and order_ingredient_milk > origin_ingredient_milk:
        return '😯 Sorry there is not enough milk!'
    return 'sufficient'

# Create function which calc the order price and process needed coins.
def process_coins():
    """Calculate the order price and process needed coins for a drink."""
    # Prompt the user to insert coins.
    print('💱 Please insert coins.')
    quarters = float(input('  how many quarters?: '))
    dimes = float(input('  how many dimes?: '))
    nickles = float(input('  how many nickles?: '))
    pennies = float(input('  how many pennies?: '))
    quarters_total = quarters * 0.25
    dimes_total = dimes * 0.1
    nickles_total = nickles * 0.05
    pennies_total = pennies * 0.01
    order_total_coins = quarters_total + dimes_total + nickles_total + pennies_total
    return order_total_coins

# Create function which that the user has inserted enough money to purchase the drink they selected.
def check_transaction(product, inserted_coins):
    """Calculate that the user has inserted enough money to purchase a drink."""
    product_cost = MENU[product]["cost"]
    if inserted_coins == product_cost or inserted_coins > product_cost:
        return True
    else:
        return False

# Create function which make the drink the user selected.
def make_coffee(resources_input, drink):
    """Make the drink the user selected."""
    milk = False
    # If the transaction is successful and there are enough resources to make the drink the
    # user selected, then the ingredients to make the drink should be deducted from the
    # coffee machine resources.
    drink_water = MENU[drink]["ingredients"]['water']
    drink_coffee = MENU[drink]["ingredients"]['coffee']
    if drink == 'latte' or drink == 'cappuccino':
        milk = True
        drink_milk = MENU[drink]["ingredients"]['milk']

    # Calculate the machine resources and ingredients after successful provision of selected drink
    resources_input['water'] -= drink_water
    resources_input['coffee'] -= drink_coffee
    if milk:
        resources_input['milk'] -= drink_milk
    # Return the updated machine resources
    return resources_input

def order_drink():
    coffee_order_continue = True
    profit = 0
    machine_resources = increase_resources(resources)
    successful_message = False
    change = 0
    prepared_drink = ''
    print_status_report = ''
    transaction_failed = False
    resources_insufficient = ''
    while coffee_order_continue:
        # Include an ASCII art logo
        print(logo)
        # Print successful message when user drink is provisioned
        if successful_message:
            if change > 0:
                print(f"💸 Here is ${round(change, 2)} in change.")
                change = 0
            print(f"Here is your {prepared_drink} ☕. Enjoy!")
            successful_message = False
        # Print report message when user ordered it
        if len(print_status_report) > 0:
            print('🖨️ Status report of machine resources:')
            for key, value in print_status_report.items():
                print(f"  {key}: {value}")
            print_status_report = ''
        if transaction_failed:
            print("💰 Sorry that's not enough money. Money refunded.")
            transaction_failed = False
        # Print status message when resources are insufficient
        if len(resources_insufficient) > 0:
            print(resources_insufficient)
            resources_insufficient = ''
        # Prompt user by asking “What would you like? (espresso/latte/cappuccino).
        user_choice = input("  📤 What would you like? (espresso/latte/cappuccino): ")
        # Check the user’s input to decide what to do next.
        user_order = check_input(user_choice)
        # The prompt should show every time action has completed, e.g. once the drink is dispensed.
        # The prompt should show again to serve the next customer.
        if user_order != 'turn_off' and user_order != 'report':
            check_resources = check_resources_sufficient(user_order, machine_resources)
            if check_resources == 'sufficient':
                order_coins_total = process_coins()
                transaction = check_transaction(user_order, order_coins_total)
                if transaction:
                    profit += MENU[user_choice]["cost"] # The cost of the drink gets added to the machine as the profit and this will be reflected the next time “report”
                    machine_resources = make_coffee(machine_resources, user_order)
                    successful_message = True
                    prepared_drink = user_order
                    if order_coins_total > MENU[user_order]["cost"]:
                        # If the user has inserted too much money, the machine should offer change.
                        change = order_coins_total - MENU[user_order]["cost"]
                else:
                    transaction_failed = True
            else:
                resources_insufficient = check_resources
        elif user_order == 'turn_off':
            coffee_order_continue = False # Turn off the Coffee Machine by entering “off” to the prompt.
        else:
            print_status_report = print_report(machine_resources, profit)
        clear()
order_drink()