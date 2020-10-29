"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit E take-home assignment
"""

"""
Write a script that plays a simple guessing game. 
The script will generate a secret number from 1 to 100, inclusive, and the user will have to guess the number. 
After each guess, the script will tell the user if they are high, low, or correct. 
If they are correct, the script will congratulate the user, tell them how many guesses they took, and then end the script. 

Hint: most of the game code will be in a loop that repeats until the correct number is guessed. 

To generate the secret number, you will need to use the randint function from Python's Random module, as follows: 

import random

#this generates a random int from 1-100, inclusive
secretNum = random.randint(1,100)
"""

import random

print("Welcome to the guessing game.")
print("You need to guess a number from 1 to 100.")

count = 0
guessNum = 0
secretNum = random.randint(1, 100)

while guessNum != secretNum:
    count += 1

    guessNum = int(input("What is your guess? "))
    if guessNum < secretNum:
        print("Guess is too low.")
    elif guessNum > secretNum:
        print("Guess is too high.")
    else:
        print("Congratulations!")
        print(f"You guessed the secret number in {count} guesses!")


"""
Execution results:

Welcome to the guessing game.
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too high.
What is your guess? 25
Guess is too high.
What is your guess? 12
Congratulations!
You guessed the secret number in 3 guesses!
"""
