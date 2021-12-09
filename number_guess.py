# Welcome to day 12 of 100 days of code. This project is a number guess game
# that allows the user to play against the computer guessing until they run out
# of lives.

# import of any modules needed including random and the logo from a different
# file.
import random
from logo import logo

# Printing the welcome statement and logo
print("Welcome to Number Guess!")
print(logo)

# Creating global variables of a list of numbers from 1 to 100 and choosing a
# random number to use in later functions.
numset = [num for num in range(1,101)]
computer_number = random.choice(numset)

# Main Game Function
def game_play():
    # Ask the user what difficulty the user would like to play
    difficulty = input('Would you like to play on Easy, Medium, or Hard? Type "E", "M" or "H"\n').lower()

    # If the user choses easy give them 10 lives and print lives
    if difficulty == "e":
        lives = 10
        first_guess = int(input(f"Guess a number from 1 to 100, you have {lives} lives.\n"))

    # If the user choses medium give them 7 lives and print lives
    elif difficulty == "m":
        lives = 7
        first_guess = int(input(f"Guess a number from 1 to 100, you have {lives} lives.\n"))

    # If the user choses hard give them 5 lives and print lives
    else:
        lives = 5
        first_guess = int(input(f"Guess a number from 1 to 100, you have {lives} lives.\n"))

    # While loop to determine how close the user is to the correct guess
    while lives != 0:
        # If the user guesses low, print their guess outcome
        if first_guess < computer_number:
            print("Your Guess was too low. Try again\n")

        # If the user guesses high, print their guess outcome
        elif first_guess > computer_number:
            print("Your guess was too high. Try again\n")

        # If the user guesses correctly, print their guess outcome and end
        # the game
        elif first_guess == computer_number:
            print("You have guessed correctly! You Win!")
            break

        # This removes a life after each guess and prints the remaining lives
        lives -= 1
        print(f"You have {lives} lives left.")

        # If the user runs out of lives end the game
        if lives == 0:
            print("You have no more lives left.")
            break

        # Ask the user for their next guess and then set that guess for the
        # program
        next_guess = int(input("Whats your next guess?\n"))
        first_guess = next_guess

# Call the main game function
game_play()

# This loop allows the game to be replayed after winning or loosing.
while True:

    # Get the users input for another game, if yes allow them to play again. If
    # no, end the program
    if input('Would you like to play again? "Yes" or "No"\n').lower() == "yes":
        print("Welcome to Number Guess!")
        print(logo)
        game_play()

    else:
        break
