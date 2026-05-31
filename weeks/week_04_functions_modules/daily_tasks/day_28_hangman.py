"""
Day 28 Milestone Project: Word Guessing (Hangman CLI) 🎯
--------------------------------------------------------
Apply modular design, local scopes, helper functions, and custom imports 
by engineering a command-line Hangman game.

Task Requirements:
1. Load a list of secret words from a random word list (or declare locally).
2. Separate core concerns into clean, dedicated helper functions:
   - get_random_word(word_list) -> str: Pick a secret word.
   - display_board(hidden_word, guessed_letters): Print the underscored status.
   - make_guess(already_guessed) -> str: Take validated unique letter from user.
   - run_game(): Main execution orchestrator.
3. Track attempts remaining (limit to 6 failed guesses).
"""

import random

WORDS = ["python", "variable", "function", "decorator", "database", "endpoint"]

def get_random_word():
    # TODO: Pick a random string from the WORDS list
    return "python"

def display_board(word, guessed_letters):
    # TODO: Loop through characters in word. If character is in guessed_letters, 
    # print it. Else, print an underscore '_'. Join elements with spaces.
    pass

def make_guess(guessed_letters):
    # TODO: In a loop:
    # 1. Ask the user for a letter
    # 2. Convert to lowercase
    # 3. Check that it is exactly 1 alphabetic character
    # 4. Check if it has already been guessed. If yes, inform user.
    # 5. If input is valid, return the letter.
    return 'a'

def run_game():
    print("=== Welcome to Hangman! ===")
    word = get_random_word()
    guessed_letters = set()
    failed_attempts = 0
    max_failed_attempts = 6
    
    # TODO: Write main game loop:
    # 1. Display the board status
    # 2. Ask user for a valid guess
    # 3. Add guess to guessed_letters
    # 4. If guess is NOT in word, increment failed_attempts
    # 5. Check victory conditions (all letters guessed)
    # 6. Check lose conditions (failed_attempts == max_failed_attempts)
    pass

if __name__ == "__main__":
    run_game()
