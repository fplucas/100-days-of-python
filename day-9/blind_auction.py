from os import system
from art import logo

still_bidding = True
bids = {}
highest_bid = 0

print(logo)
print("Welcome to the secret auction program.")
while still_bidding:
    name = input("What is your Name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    still_bidding = input(
        "Are there any other bidders? Type 'yes' or 'no'.\n") == 'yes'
    system('clear')

for bidders in bids:
    name = bidders
    bid = bids[bidders]
    if bid > highest_bid:
        winner = name

print(f"The winner is {name} with a bid of ${bids[name]}.")
