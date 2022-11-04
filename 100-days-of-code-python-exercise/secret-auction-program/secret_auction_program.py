from replit import clear
from art import logo
from operator import itemgetter

print(logo)
print("Welcome to the secret auction program")

# Declare dictionary to store the player bids
auction_dict = {}

# Create function to store into auction_dict the player bids
def secret_auction(player, bid):
    # Extract only the digits from the bid input string and remove any other char and symbols
    num = ''
    for digit in bid:
        if digit.isdigit():
            num += digit
    auction_dict[player] = int(num)

# Create function to calculate the highest(winner) player bid
def highest_bidder():
    # Using sorted() function to sort auction_dict by value in descending order
    sort_auction_dict= dict(sorted(auction_dict.items(), key=itemgetter(1), reverse=True))

    # Using next() + iter() to get the first(highest) key:value in auction_dict
    winner = next(iter(sort_auction_dict))
    print(f"The winner is {winner} with a bid of ${sort_auction_dict[winner]}.")

bidders = True

# Create a while loop to provide continues functionality until there are no more bids
while bidders:

    player_name = input("What is your name?: ")
    player_bid = input("What is your bid?: ")

    secret_auction(player=player_name, bid=player_bid)

    bid_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    if bid_continue == 'no':
        bidders = False

    # Clear the terminal to remove the last player bid
    clear()

# Exit the auction and print the winner
if not bidders:
    highest_bidder()
