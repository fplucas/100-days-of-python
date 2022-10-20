from os import system
from art import logo, vs
from game_data import data
from random import choice


def guessed_right(compare, answer):
    if (compare[0]['follower_count'] > compare[1]['follower_count']):
        right_answer = 'a'
    else:
        right_answer = 'b'
    return answer == right_answer


def print_compare(compare, option):
    print(
        f"Compare {option}: {compare['name']}, a {compare['description']}, from {compare['country']}.")


def new_turn():
    answer = 'c'
    compare = []
    for index in range(2):
        compare.append(choice(data))
    print(logo)
    # print(compare[0]['follower_count'], compare[1]['follower_count'])
    print_compare(compare[0], 'A')
    print(vs)
    print_compare(compare[1], 'B')
    while not answer in 'ab':
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    system('clear')
    return guessed_right(compare, answer)


def play():
    score = 0
    while new_turn():
        score += 1
        print(f"You're right! Current score: {score}.")
    print(f"Sorry, that's wrong. Final score: {score}.")


play()
