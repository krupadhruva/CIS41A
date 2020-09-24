"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit C take-home assignment
"""

"""
Second Script – Bit Operators

Assign the values 9 and 14 to variables a and b respectively.
Print the binary values of a and b (use the bin built-in function).
Calculate the value of a and b, print the result in binary.
Calculate the value of a or b, print the result in binary.
Examine the results. Can you see how they were arrived at?
Example output:

b) binary of a =  0b1001
b) binary of b =  0b1110
c) binary of a & b =  0b1000
d) binary of a | b =  0b1111
Add the following at the end of the script to show your results:
"""

a = 9
b = 14

print(f"binary of a = {bin(a)}")

print(f"binary of b = {bin(a)}")

print(f"binary of a & b = {bin(a & b)}")

print(f"binary of a | b = {bin(a | b)}")

""" 
Execution results:

binary of a = 0b1001
binary of b = 0b1001
binary of a & b = 0b1000
binary of a | b = 0b1111
"""
