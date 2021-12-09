import random
from logo import logo


print("Welcome to Number Guess!")
print(logo)

numset = [num for num in range(1,101)]
computer_number = random.choice(numset)
def game_play():
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


    while lives != 1:
        if first_guess < computer_number:
            print("Your Guess was too low. Try again\n")
        elif first_guess > computer_number:
            print("Your guess was too high. Try again\n")
        elif first_guess == computer_number:
            print("You have guessed correctly! You Win!")
            break
        lives -= 1
        if lives ==1:
            print("You have no more lives left.")
            break
        next_guess = int(input("Whats your next guess?\n"))
        first_guess = next_guess

game_play()

while True:
    if input('Would you like to play again? "Yes" or "No"\n').lower() == "yes":
        print("Welcome to Number Guess!")
        print(logo)
        game_play()
    else:
        break

# Setting Up structure

# Tasklist:
# Comments and welcome statement
