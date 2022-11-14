############### Number Guessing Project #####################
from art import logo
from random import randint

# Declare a global variables
LEVEL_EASY = 10
LEVEL_HARD = 5
GUESSED_NUMBER = True

# Create function that calculate and compare player guess number and generated number.
def compare_numbers(player_n, generated_n):
    if player_n > generated_n:
        print("Too high.")
    elif player_n < generated_n:
        print("Too low.")
    else:
        # If the player got the answer correct, show the actual answer to him and the game ends.
        print( f"You got it! The answer was {generated_n}.")
        return GUESSED_NUMBER

# Create function that include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def difficulty_level():
    difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
    if difficulty == 'easy':
        return LEVEL_EASY
    elif difficulty == 'hard':
        return LEVEL_HARD

# Create function that would provide configurations and run the number guessing game.
def run_game():
    # Include an ASCII art logo.
    print(logo)

    # Print welcome message to the game.
    print("Welcome to the Number Guessing Game!")

    # Use random to generate number.
    print("I'm thinking of a number between 1 and 100.")
    generated_number = randint(1, 100)

    # Provide game level choice (easy or hard to the user).
    level = difficulty_level()

    count = 0
    attempt = level

    while count < level:
        # Allow the player to submit a guess for a number between 1 and 100.
        player_guess = int(input(f"You have {attempt} attempts remaining to guess the number.\nMake a guess: "))
        if player_guess < 1 or player_guess > 100:
            print("Your choice is outside of the provided range between 1 and 100. The game ends.")
            return
        else:
            # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
            result = compare_numbers(player_guess, generated_number)
            # Check user's guess against actual answer if it's right one the game ends with player win.
            if result == GUESSED_NUMBER:
                return
            else:
                # Track the number of turns remaining.
                count += 1
                attempt -= 1
                if attempt != 0:
                    print(f"Guess again.")

    # If they player is out of available turns, provide feedback to the user.
    print("You've run out of guesses, you lose.")

# This is the execution of the function that would run the number guessing game.
run_game()