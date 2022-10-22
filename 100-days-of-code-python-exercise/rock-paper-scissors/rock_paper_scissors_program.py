import random

# Declare ascii art variables
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create list of game elements covered by the declared ascii art variables
game_elements = [rock, paper, scissors]
user_input = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))
computer_input = random.randint(0, 2)

# Iterate over the user and computer input to do a match the choice and define the game output
if user_input > 2 or user_input < 0:
    print("User input is invalid. Restart the game!")
else:
    print(game_elements[user_input])
    print('Computer chose: \n')
    print(game_elements[computer_input])

    if user_input == 0 and computer_input == 2:
        print("The game is over. You win the game.")
    elif user_input == 2 and computer_input == 1:
        print("The game is over. You win the game.")
    elif user_input > computer_input:
        print("The game is over. You lost the game.")
    elif user_input < computer_input:
        print("The game is over. You lost the game.")
    elif user_input == computer_input:
        print("The game is over. The result is draw.")
