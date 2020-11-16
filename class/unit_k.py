"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit K in-class assignment
"""

import random

"""
Part 1 of 1 - Generating Unique Random Numbers

Generate ten random but unique numbers that range from 1 to 15 inclusive. 
Print the sorted numbers.

Hint: Use one of the methods from Python's random module.

Optional Challenge: Do this with one line of code.
"""

print(sorted(random.sample(range(1, 16), 10)))

"""
Execution results:

[2, 3, 6, 7, 8, 10, 11, 12, 14, 15]
"""
