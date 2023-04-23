# Python Wordle Helper - ChatGPT

## Prompt

can you help me write a python program that helps solve wordle puzzles?

## Response

Sure, I can help you with that! Wordle is a popular word puzzle game where players have to guess a five-letter word with limited guesses. Here's a Python program that can help solve Wordle puzzles:

```text
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
```

To use this program, simply run it in a Python interpreter or in a terminal. The program will generate a random five-letter word from a list of words and prompt the user to guess the word. The user has five chances to guess the word, and after each guess, the program will display the number of bulls and cows (correct letters in the correct position and correct letters in the wrong position, respectively).

I hope this helps you solve some Wordle puzzles!

## Results
