"""
Day 14 Milestone Project: The Number Guessing Game 🎮
------------------------------------------------------
Consolidate conditionals, boolean logic, while loops, and importing modules 
by engineering a command-line Number Guessing Game.

Task Requirements:
1. Import the 'random' module to pick a secret number between 1 and 100.
2. Allow the player up to 7 attempts to guess the number.
3. In a loop:
   - Ask the player for their guess.
   - Cast the guess to an integer.
   - If correct: Print a success message, reveal the number of guesses taken, and exit.
   - If incorrect: Inform them if the guess was "Too High" or "Too Low", and decrement remaining attempts.
4. If they run out of attempts without guessing correctly, print "Game Over" and reveal the secret number.

Run and test the game in the terminal!
"""

import random

def play_game():
    print("=== Welcome to the Number Guessing Game! ===")
    print("I have chosen a secret number between 1 and 100.")
    print("Can you guess it within 7 attempts?\n")
    
    # TODO 1: Generate a random secret number using random.randint()
    secret_number = 0
    attempts_left = 7
    
    # TODO 2: Loop until attempts run out or player guesses the secret number
    # Use a while loop to keep track of guesses and attempts left.
    
    # TODO 3: Track conditions (Correct, Too High, Too Low)
    
    # TODO 4: Display GameOver message if attempts reach 0

if __name__ == "__main__":
    play_game()
