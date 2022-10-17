from os import system
import random

BLACKJACK = 21
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def went_over(cards, limit=BLACKJACK):
    if (sum(cards) > limit and 11 in cards):
        cards[cards.index(11)] = 1
    return sum(cards) > limit


def get_random_card():
    return random.choice(CARDS)


def get_dealer_cards():
    cards = [get_random_card(), get_random_card()]
    while (not went_over(cards, 17)):
        cards.append(get_random_card())
    return cards


def end_of_game(player_cards, dealer_cards):
    player_final_score = sum(player_cards)
    dealer_final_score = sum(dealer_cards)
    print(
        f"Your final hand: {player_cards}, final score: {player_final_score}")
    print(
        f"Computer's final hand: {dealer_cards}, final score: {dealer_final_score}")
    if (player_final_score == BLACKJACK):
        print("BlackJack! You win!")
    elif (went_over(player_cards)):
        print("You went over. You lose")
    elif (went_over(dealer_cards)):
        print("Dealer went over. You win")
    elif (player_final_score == dealer_final_score):
        print("It is a draw")
    elif (player_final_score > dealer_final_score):
        print("You scored more than the dealer. You win")
    else:
        print("The dealer scored more than you. You lose")
    input()
    new_game()


def play():
    player_cards = [get_random_card()]
    dealer_cards = get_dealer_cards()
    get_another_card = 'y'
    while get_another_card == 'y':
        player_cards.append(get_random_card())
        print(
            f"Your cards: {player_cards}, current score {sum(player_cards)}")
        print(f"Computer's first hand card: {dealer_cards[0]}")
        if (sum(player_cards) == 21 or went_over(player_cards)):
            end_of_game(player_cards, dealer_cards)
        get_another_card = input(
            "Type 'y' to get another card, type 'n' to pass: ")
    end_of_game(player_cards, dealer_cards)


def new_game():
    system('clear')
    want_to_play = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y'

    if (want_to_play):
        play()


new_game()
