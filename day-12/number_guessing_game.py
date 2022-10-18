from random import randrange


def get_number_of_attempts():
    difficulty = ""
    while difficulty not in ('easy', 'hard'):
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if (difficulty == 'easy'):
        return 10
    return 5


def get_random_number():
    return randrange(100)


def guess(guessed_number, chosen_number):
    if (guessed_number == chosen_number):
        print(f"You got it! The answer was {chosen_number}.")
        play()
    elif (guessed_number > chosen_number):
        print("Too high.")
    else:
        print("Too low.")
    print("Guess again.")


def play():
    play_again = 'y'
    while play_again == 'y':
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")
        number_of_attempts = get_number_of_attempts()
        random_number = get_random_number()
        while number_of_attempts > 0:
            print(
                f"You have {number_of_attempts} attempts remaining to guess the number.")
            guess(int(input('Make a guess: ')), random_number)
            number_of_attempts -= 1
        print("You lost.")
        play_again = input("Type 'y' to play again or hit Enter to end: ")


play()
