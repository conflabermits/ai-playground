#!/usr/bin/env python3
import random

def get_word():
    # This function generates a random five-letter word from a list of words.
    word_list = ["apple", "banana", "cherry", "grape", "kiwi", "lemon", "melon", "orange", "peach", "pear"]
    return random.choice(word_list)

def check_guess(word, guess):
    # This function checks the guessed word against the actual word and returns a tuple of bulls and cows.
    # A bull is a correct letter in the correct position, while a cow is a correct letter in the wrong position.
    bulls = 0
    cows = 0
    for i in range(len(word)):
        if word[i] == guess[i]:
            bulls += 1
        elif guess[i] in word:
            cows += 1
    return (bulls, cows)

def main():
    # This function runs the main game loop.
    print("Welcome to Wordle!")
    word = get_word()
    guesses = 0
    while guesses < 5:
        guess = input("Guess a five-letter word: ")
        if guess == word:
            print("Congratulations, you win!")
            return
        bulls, cows = check_guess(word, guess)
        print(f"{bulls} bulls, {cows} cows")
        guesses += 1
    print(f"Sorry, you lose! The word was {word}.")

if __name__ == "__main__":
    main()
