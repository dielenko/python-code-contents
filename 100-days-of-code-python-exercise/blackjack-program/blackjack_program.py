############### Blackjack Project #####################
from replit import clear
import random
from deck import cards
from art import logo

blackjack = True
game_continue = True

while blackjack:
    print(logo)
    def deal_card():
        card_choice = random.choice(cards)
        return card_choice

    # Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []

    draw_run = 0
    for el in range(0,2):
        if draw_run == 1:
            el +=1
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    draw_run = 1

    # Create a function called calculate_score() that takes deck_list of cards as input and returns the score.
    # Use the sum() function to calculate the list items in total.
    def calculate_score(deck_list):
        ace = 11
        score = sum(deck_list)

        # Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in the game.
        # Use count() to check the number of times element exists in deck_list
        ace_count = deck_list.count(ace)
        if len(deck_list) == 2 and ace_count > 0 and score == 21:
            score = 0
        # Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. Use the append() and remove() to achieve that goal.
        elif score > 21:
            for card in deck_list:
                if card == ace:
                        deck_list.remove(card)
                        deck_list.append(1)
            score = sum(deck_list)
        return score

    # Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    def checked_score(game_continue):
        return_checked_score = []
        while game_continue:
            user_score = calculate_score(user_cards)
            print(f"    Your cards: {user_cards}, current score: {user_score}")
            computer_score = calculate_score(computer_cards)
            print((f"    Computer's first card: {computer_cards[0]}"))
            if user_score == 0 or user_score > 21 or computer_score == 0:
                game_continue = False
            else:
                # If the game has not ended, ask the user if they want to draw another card. 
                # If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
                draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if draw_another_card == 'y':
                    user_cards.append(deal_card())
                else:
                    game_continue = False
        return_checked_score.append(user_score)
        return_checked_score.append(computer_score)
        return return_checked_score

    # The score will need to be rechecked with every new card drawn and the checks with checked_score() and calculate_score() need to be repeated until the game ends.
    final_score = checked_score(game_continue)

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    calculated_user_score = final_score[0]
    calculated_computer_score = final_score[1]
    while calculated_user_score != 0 and calculated_computer_score !=0 and calculated_computer_score < 17:
        computer_cards.append(deal_card())
        calculated_computer_score = calculate_score(computer_cards)

    # Create a function called compare() and pass in the user_score and computer_score. 
    # If the computer and user both have the same score, then it's a draw.
    # If the computer has a blackjack (0), then the user loses. 
    # If the user has a blackjack (0), then the user wins. 
    # If the user_score is over 21, then the user loses. 
    # If the computer_score is over 21, then the computer loses. 
    # If none of the above, then the player with the highest score wins.
    def compare(user_score, computer_score):
        if user_score <= 21 and computer_score <= 21 and user_score == computer_score:
            print("It's a draw")
        elif computer_score == 0:
            print("Lose, opponent has Blackjack 😱")
        elif user_score == 0:
            print("Win, you have Blackjack 😱")
        elif user_score > 21:
            print("You went over. You lose 😭")
        elif computer_score > 21:
            print("Opponent went over. You win 😁")
        elif user_score > computer_score:
            print("You win 😃")
        else:
            print("You lose 😤")

    # Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
    print(f"    Your final hand: {user_cards}, final score: {calculated_user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {calculated_computer_score}")
    compare(calculated_user_score, calculated_computer_score)
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == 'y':
        clear()
    else:
        blackjack = False


