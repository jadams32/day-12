import random
from logo import logo


print("Welcome to Number Guess!")
print(logo)

numset = [num for num in range(1,101)]
computer_number = random.choice(numset)

difficulty = input('Would you like to play on Easy, Medium, or Hard? Type "E", "M" or "H"\n').lower()

if difficulty == "e":
    lives = 10
    first_guess = int(input(f"Guess a number from 1 to 100, you have {lives} lives.\n"))
elif difficulty == "m":
    lives = 7
    first_guess = int(input(f"Guess a number from 1 to 100, you have {lives} lives.\n"))
else:
    lives = 5
    first_guess = int(input(f"Guess a number from 1 to 100, you have {lives} lives.\n"))


# Setting Up structure

# Tasklist:
# ask the user to input their guess and remove a life
# check if the guess matches and report either high or low to the user
# if the user guesses correctly print you win
# ask the user if they would like to play again
# if yes repeat program, if no exit.
