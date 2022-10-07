from os import system
from hangman_art import stages, logo
from hangman_words import word_list
import random

word = list(random.choice(word_list))
lives = 6
masked_word = list("_" * len(word))
guessed_letters = []

def letter_in_the_word(guess):
    if guess in guessed_letters:
        print("You have already guessed this letter")
    elif guess in word:
        for index in range(len(word)):
            if(guess == word[index]):
                masked_word[index] = word[index]
    else:
        return False
    return True

def won():
    return not "_" in masked_word

def lost():
    return lives <= 0

def still_playing():
    return not won() and not lost()

while still_playing():
    system('clear')
    print(logo)
    print(f"Lives: {lives}")
    print(masked_word)
    print(stages[lives])
    guess = input("Guess a letter: ").lower()
    if not letter_in_the_word(guess):
        lives -= 1

print(word)
if won():
    print("Congratulations, you won!")
else:
    print("You lost")
