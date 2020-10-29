"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit E in-class assignment
"""

"""
1) Using range with a for loop.

Use a for loop to print the even integers in descending order from 10 to 0 inclusive.
2) Looping through dictionary items.

Create a dictionary named movies and populate it with these key value pairs: 
The Wizard of Oz:1939 
The Godfather:1972 
Lawrence of Arabia:1962 
Raging Bull:1980 
Loop through the dictionary items and print the year in which each movie was made. Output should be alpha sorted by movie title.
"""

# Use a for loop to print the even integers in descending order from 10 to 0 inclusive.
for even in range(10, -1, -2):
    print(even)

"""
Create a dictionary named movies and populate it with these key value pairs: 
The Wizard of Oz:1939 
The Godfather:1972 
Lawrence of Arabia:1962 
Raging Bull:1980 
"""
movies = {
    "The Wizard of Oz": 1939,
    "The Godfather": 1972,
    "Lawrence of Arabia": 1962,
    "Raging Bull": 1980,
}

# Loop through the dictionary items and print the year in which each movie was made.
# Output should be alpha sorted by movie title.
for key in sorted(movies.keys()):
    print(f"{key} was made in {movies.get(key)}")

"""
Execution results:

10
8
6
4
2
0
Lawrence of Arabia was made in 1962
Raging Bull was made in 1980
The Godfather was made in 1972
The Wizard of Oz was made in 1939

"""
