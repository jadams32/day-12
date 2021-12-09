import random
from logo import logo

numset = [num for num in range(1,101)]

print("Welcome to Number Guess!")
print(logo)

difficulty = input('Would you like to play on Easy, Medium, or Hard? Type "E", "M" or "H"\n').lower()
easy_lives = 10
medium_lives = 7
hard_lives = 5
if difficulty == "e":
    print(f"Guess a number from 1 to 100, you have {easy_lives} lives.")
elif difficulty == "m":
    print(f"Guess a number from 1 to 100, you have {medium_lives} lives.")
else:
    print(f"Guess a number from 1 to 100, you have {hard_lives} lives.")

# Setting Up structure

# Tasklist:
# pick a number from a list of 1 to 100 for the user to guess
# ask the user to input their guess and remove a life
# check if the guess matches and report either high or low to the user
# if the user guesses correctly print you win
# ask the user if they would like to play again
# if yes repeat program, if no exit.
