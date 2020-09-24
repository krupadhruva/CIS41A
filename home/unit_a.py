"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit A take-home assignment
"""


import math


"""
Basic math and string operations

Calculate and print the final value of each variable.

a equals 3 to the power of 2.5
b equals 2 b equals b + 3 (use +=)
c equals 12 c = c divided by 4 (use /=)
d equals the remainder of 5 divided by 3
"""


# Based on the longest label we print
pad = 75
separator = ":"


a = math.pow(3, 2.5)
label = "a equals 3 to the power of 2.5"
print(f"{label+separator:<{pad}}{a}")

b = 2
b += 3
label = "b equals 2 b equals b + 3 (use +=)"
print(f"{label+separator:<{pad}}{b}")

c = 12
c /= 4
label = "c equals 12 c = c divided by 4 (use /=)"
print(f"{label+separator:<{pad}}{c}")

d = 5 % 2
label = "d equals the remainder of 5 divided by 3"
print(f"{label+separator:<{pad}}{d}")


"""
Built-in functions abs, round, and min

Use abs, round, and min to calculate some values. These are all Python built in functions (see: BIF ).

Print the difference between 5 and 7.
Print 3.14159 rounded to 4 decimal places.
Print 186282 rounded to the nearest hundred.
Print the minimum of 6, -9, -3, 0
"""
print()

val = abs(5 - 7)
label = "Print the difference between 5 and 7"
print(f"{label+separator:<{pad}}{val}")

val = 3.14159
label = "Print 3.14159 rounded to 4 decimal places"
print(f"{label+separator:<{pad}}{val:.2f}")

val = round(186282 / 100) * 100
label = "Print 186282 rounded to the nearest hundred"
print(f"{label+separator:<{pad}}{val}")

val = min(6, -9, -3, 0)
label = "Print the minimum of 6, -9, -3, 0"
print(f"{label+separator:<{pad}}{val}")


"""
Functions from the math module

Use some functions from Pythons math module to perform some calculations.

Ask the user for a number (test with the value 7.6).
Print the square root of the number, rounded to two decimal places (include an appropriate description).
Print the base-10 log of the number, rounded to two decimal places (include an appropriate description) 
(see https://docs.python.org/3/library/math.html).
"""
print()

val = input("Enter a number: ")
try:
    # Check if the entered number is a valid number, raises exception ValueError on failure
    num = float(val)
    num = math.sqrt(num)
    label = "Print the square root of the number, rounded to two decimal places"
    print(f"{label + separator:<{pad}}{num:.2f}")

    label = "Print the base-10 log of the number, rounded to two decimal places"
    num = math.log(num, 10)
    print(f"{label + separator:<{pad}}{num:.2f}")
except ValueError:
    print(f"invalid entry: {val} is not a valid number")


"""
Complex numbers

Do a calculation with complex numbers. Note that, while you might be familiar with the notation convention commonly used within mathematics for complex numbers (z = a + bi), Python uses the notation convention used in electromagnetism and electrical engineering (z = a + bj).

Assign z1 the value of 4 + 3j
Assign z2 the value of 2 + 2j
Assign z3 the value of z1 times z2
Print the value of z3
"""
print()

z1 = 4 + 3j
z2 = 2 + 2j
z3 = z1 * z2
label = "Print the value of z3"
print(f"{label+separator:<{pad}}{z3}")


"""
Execution results:

a equals 3 to the power of 2.5:                                            15.588457268119896
b equals 2 b equals b + 3 (use +=):                                        5
c equals 12 c = c divided by 4 (use /=):                                   3.0
d equals the remainder of 5 divided by 3:                                  1

Print the difference between 5 and 7:                                      2
Print 3.14159 rounded to 4 decimal places:                                 3.14
Print 186282 rounded to the nearest hundred:                               186300
Print the minimum of 6, -9, -3, 0:                                         -9

Enter a number: 7.6
Print the square root of the number, rounded to two decimal places:        2.76
Print the base-10 log of the number, rounded to two decimal places:        0.44

Print the value of z3:                                                     (2+14j)
"""
