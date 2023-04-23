# Python Wordle Helper - ChatGPT

## Prompt

can you help me write a python program that helps solve wordle puzzles?

## Response

Sure, I can help you with that! Wordle is a popular word puzzle game where players have to guess a five-letter word with limited guesses. Here's a Python program that can help solve Wordle puzzles:

```python
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

First off, it was clear there were some issues with the code. The word list contained 4-letter and 6-letter words despite calling out that it should contain 5-letter words. It checks for "bulls" and "cows", and defines them in the code, but doesn't define them for the user. Plus it doesn't tell the user which letter spots within a word were bulls vs cows. It also doesn't tell the user how many guesses they have left. Finally, it doesn't tell the user if they guessed the same word twice.

On first run, it errored-out:

```text
$ ./gpt-wordle.py 
Welcome to Wordle!
Guess a five-letter word: kiwi
Traceback (most recent call last):
  File "/local/git/ai-playground/./gpt-wordle.py", line 37, in <module>
    main()
  File "/local/git/ai-playground/./gpt-wordle.py", line 31, in main
    bulls, cows = check_guess(word, guess)
  File "/local/git/ai-playground/./gpt-wordle.py", line 15, in check_guess
    if word[i] == guess[i]:
IndexError: string index out of range
```

The error occurs because the length of the guess ("kiwi", 4 letters) did not match the length of the word ("apple", 5 letters). The program tries to iterate over the length of the word (`range(0, 5)`, or `0` through `4`) and trips over itself when it reaches index `4` because it doesn't exist on the guess word.

After adjusting the `word_list` array to only contain 5-letter words, the program ran successfully:

```text
$ ./gpt-wordle.py 
Welcome to Wordle!
Guess a five-letter word: lemon
0 bulls, 1 cows
Guess a five-letter word: melon
0 bulls, 1 cows
Guess a five-letter word: apple
1 bulls, 3 cows
Guess a five-letter word: grape
Congratulations, you win!
```

The program ran successfully to completion (a win), but still had some fault logic surrounding the "bulls" and "cows". In the penultimate guess, "apple", the response tells the user there are "1 bulls, 3 cows", but that's not 100% correct. Knowing the correct guess is "grape", we can tell the bull is the "e", which is the correct letter in the correct position. However, there are technically only two "cows", the "a" and one of the "p" letters. The word "grape" only has one "p", and in Worlde proper it would only report one of those letters as a cow, not both.

On a successful run to completion that's a loss, it does what it's programmed to do, but this highlights the flaws noted earlier about not checking if the word has already been guessed. I guess the silver lining is that it makes it easier to speedrun a loss.

```text
$ ./gpt-wordle.py 
Welcome to Wordle!
Guess a five-letter word: mario
0 bulls, 1 cows
Guess a five-letter word: mario
0 bulls, 1 cows
Guess a five-letter word: mario
0 bulls, 1 cows
Guess a five-letter word: mario
0 bulls, 1 cows
Guess a five-letter word: mario
0 bulls, 1 cows
Sorry, you lose! The word was peach.
```
