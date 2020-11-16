"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit J take-home assignment
"""

import random

"""
Part 1 of 1 - Nested Loop Dice Game

Write a script that simulates a simple dice gambling game.

The game is played as follows: roll a six sided die. 
If you roll a 1, 2 or a 3, the game is over. 
If you roll a 4, 5, or 6, you win that many dollars ($4, $5, or $6), and then roll again. 
With each additional roll, you have the chance to win more money, or you might roll a game-ending 1, 2, or 3,
at which time the game is over and you keep whatever winnings you have accumulated.

Use the randint function from Python's Random module to get a die roll result 
(see functions for integers).

Run 10,000 simulations of the game (Monte Carlo method). 
Print the average amount won and the largest amount won.

Just as a thought experiment, would you pay $3 for a chance to play this game?

Example Output:

Average amount won = x.xx
Max amount won = xx
"""


def roll_dice_game(iterations: int):
    max_amount = 0
    total_amount = 0

    for _ in range(iterations):
        amount_won = 0
        while True:
            value = random.randint(1, 6)
            # If 1, 2 or 3, game over
            if value < 4:
                break

            amount_won += value

        max_amount = max(max_amount, amount_won)
        total_amount += amount_won

    return total_amount / iterations, max_amount


if __name__ == "__main__":
    # Testing: Set random generator seed for repeatable results
    # random.seed(100)

    average_amount_won, max_amount_won = roll_dice_game(10000)

    print(f"Average amount won = {average_amount_won:.2f}")
    print(f"Max amount won = {max_amount_won}")

"""
Question: Just as a thought experiment, would you pay $3 for a chance to play this game?
Response: Yes. Since the dice has 6 possibilities ranging from 1 to 6, 3 is the mid point.
Hence, in a fair game, we will have 50% chance to earn $3. Since there is not much to lose,
it is worth playing this game.
"""

"""
Execution results:

Average amount won = 4.96
Max amount won = 74
"""
