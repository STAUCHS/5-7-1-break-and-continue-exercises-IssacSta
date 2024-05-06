#-------------------------------------------------------------------------
# Name: Issac zha
# Purpose: guess the number game
# Author:     Zha. I
# Created:    06/05/2024
#-------------------------------------------------------------------------
import random

def main():
    print("Guess the Number")
    print("Welcome to the guess the number game.")
    print("You have 5 chances to guess the number between 1 and 100.\n")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Set the number of guesses allowed
    max_guesses = 5
    guesses = 0

    # Loop until the user guesses the correct number or runs out of guesses
    while guesses < max_guesses:
        guesses += 1
        guess = int(input("Enter a number between 1 and 100: "))

        if guess < secret_number:
            print("Too low, guess again")
        elif guess > secret_number:
            print("Too high, guess again")
        else:
            print("\nCongratulations! You've guessed the correct number.")
            return

    # If the loop finishes without the correct guess, print the correct number
    print(f"\nSorry, you've guessed incorrectly, the number is {secret_number}.")


