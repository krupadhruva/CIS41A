"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit B take-home assignment
"""

"""
Printing a well formatted invoice

Use three named "constants" for the following: 
small beads with a price of 9.20 dollars per box 
medium beads with a price of 8.52 dollars per box 
large beads with a price of 7.98 dollars per box 

Ask the user how many boxes of small beads, how many boxes of medium beads, and how many large beads they need (use the int Built-in Function to convert these values to int).

Print the invoice in the following format:

SIZE      QTY    COST PER BOX      TOTALS
Small       n            x.xx       xx.xx
Medium      n            x.xx       xx.xx
Large       n            x.xx       xx.xx
TOTAL                              xxx.xx
Replace the n and x placeholders with actual numeric data values. Right align all numeric values. All dollar amounts should have two decimal places and should align on the decimal point.

Test your script twice, first with user input of 10 boxes of small beads, 9 boxes of medium beads, and 8 boxes of large beads, and then a second time with user input of 5 boxes of small beads, 10 boxes of medium beads, and 15 boxes of large beads. The second test will have a slight alignment problem, Do not try to fix it now. We will learn more about formatting later.
"""


COST_SMALL_BEADS = 9.20
COST_MEDIUM_BEADS = 8.52
COST_LARGE_BEADS = 7.98


qty_small_beads = input("how many boxes of small beads: ")
qty_medium_beads = input("how many boxes of medium beads: ")
qty_large_beads = input("how many boxes of large beads: ")
print()

try:
    qty_small_beads = int(qty_small_beads)
    qty_medium_beads = int(qty_medium_beads)
    qty_large_beads = int(qty_large_beads)

    if min(qty_small_beads, qty_medium_beads, qty_large_beads) < 0:
        raise ValueError("quantity cannot be negative")
except ValueError as ex:
    print(f"invalid entry: {ex}")
    exit(-1)


buff = ("SIZE", "QTY", "COST PER BOX", "TOTALS")
print(f"{buff[0]:<10}{buff[1]:>10}{buff[2]:>15}{buff[3]:>15}")

buff = (
    "Small",
    qty_small_beads,
    COST_SMALL_BEADS,
    f"{qty_small_beads * COST_SMALL_BEADS:.2f}",
)
print(f"{buff[0]:<10}{buff[1]:>10}{buff[2]:>15}{buff[3]:>15}")

buff = (
    "Medium",
    qty_medium_beads,
    COST_MEDIUM_BEADS,
    f"{qty_medium_beads * COST_MEDIUM_BEADS:.2f}",
)
print(f"{buff[0]:<10}{buff[1]:>10}{buff[2]:>15}{buff[3]:>15}")

buff = (
    "Large",
    qty_large_beads,
    COST_LARGE_BEADS,
    f"{qty_large_beads * COST_LARGE_BEADS:.2f}",
)
print(f"{buff[0]:<10}{buff[1]:>10}{buff[2]:>15}{buff[3]:>15}")

buff = (
    "TOTAL",
    "",
    "",
    f"{(qty_small_beads * COST_SMALL_BEADS) + (qty_medium_beads * COST_MEDIUM_BEADS) + (qty_large_beads * COST_LARGE_BEADS):.2f}",
)
print(f"{buff[0]:<10}{buff[1]:>10}{buff[2]:>15}{buff[3]:>15}")

"""
Execution results:
how many boxes of small beads: 10
how many boxes of medium beads: 9
how many boxes of large beads: 8

SIZE             QTY   COST PER BOX         TOTALS
Small             10            9.2          92.00
Medium             9           8.52          76.68
Large              8           7.98          63.84
TOTAL                                       232.52
"""
