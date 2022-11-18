############### Higher Lower Project #####################
from random import choice
from art import logo, vs
from game_data import data
from replit import clear

# Create function which insert from data file option A and B for comparison
def insert_data(stored_list, count_items):
    """Get data from random account and create list called stored_list[]"""
    # Use random module with choice() to serve randomly options A and B
    if count_items < 1:
        for _ in range(2):
            random_element = choice(data)
            # Use list to store option A[0] and B[1]
            if random_element not in stored_list:
                stored_list.append(random_element)
            else:
                random_element = choice(data)
                stored_list.append(random_element)
    else:
        random_element = choice(data)
        # Use the list to store only option B[1] after the first cycle of comparison
        if random_element not in stored_list:
            stored_list.append(random_element)
        else:
            random_element = choice(data)
            stored_list.append(random_element)

    return stored_list

# Create function that serve option A and B stored in list store_options[]
def serve_options(stored_items):
    """Format option A and B stored in list store_options[] into printable format: name, description and country"""
    for option in range(len(stored_items)):
        if option == 0:
            option_name = 'Compare A'
        else:
            option_name = 'Against B'
        print(f"{option_name}: {stored_items[option]['name']}, a {stored_items[option]['description']}, from {stored_items[option]['country']}.")
        if option == 0:
            print(vs)

# Create function that compare the defined followers regarding option A and B stored in list store_options[]
def compare_followers(followers_items):
    """Checks followers against player choice and returns string regarding option A and B if they got it right."""
    # Add logic to provide functionality that defines if the player's guess is wrong/game ends or right then the game continues
    # compare_player_choice()
    for _ in followers_items:
        if followers_items[0]['follower_count'] > followers_items[1]['follower_count']:
            return 'option_a_wins'
        elif followers_items[0]['follower_count'] < followers_items[1]['follower_count']:
            return 'option_b_wins'

# Create run_game() function to execute the game
def run_game():

    count = 0
    stored_items = []
    score = 0

    while True:
        # Include an ASCII art logo
        print(logo)

        # Provide logic to calculate the points(success guessed) until the game ends with wrong answer or all options are guessed
        if count > 0:
            score += 1
            print(f"You're right! Current score: {score}.")
        # Insert from data file option A and B for comparison
        store_options = insert_data(stored_items, count)

        # Serve options A and B to provide a choice for the player to select
        serve_options(store_options)

        # Ask the player to define who has more followers from provided persons as options
        # Use upper() to provide the user input of small letters is case insensitive for the program
        # Allow the player to submit an answer for a compare (A and B)
        player_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        # Provide the results from person followers comparison
        followers_result = compare_followers(store_options)

        # Providing calculation logic of the output regarding the player choice
        if (player_choice == 'A' and followers_result == 'option_a_wins') or (player_choice == 'B' and followers_result == 'option_b_wins'):
            # B option(last inserted) stays, and randomly next option to compare will be served
            store_options.pop(0)
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            return

        # Prepare the next round to update the store options[] with only one new random option
        count += 1

        # Clear the screen between rounds
        clear()

run_game()