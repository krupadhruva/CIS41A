"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit E take-home assignment
"""

"""
Part One - Looping with String Methods

Update the Unit B Counting and Finding In-Class exercise to use a loop.

Assign the text "Believe you can and you're halfway there." to a variable called quote (this is a quote from Theodore Roosevelt).
Loop through the quote to find and print the index of all the "a" characters.

Hint: One way is to loop a fixed number of times, based on the count of the "a" characters. 
Another way is to loop until you have searched the entire string. 
It can be convenient to initialize the location variable before starting the loop.
"""

quote = "Believe you can and you're halfway there."

for idx in range(len(quote)):
    if "a" == quote[idx]:
        print(f"a found at index {idx}")


"""
Part Two - Nested Loops

Write a script using nested for loops to generate a triangular multiplication table as illustrated below. 
Ask the user how many rows they would like in their table. 
Generate formatted output where each number is right justified within a fixed field size, so that the numbers in each column are aligned. 

Test with a user value of 12 rows.

Example output:

a found at index 13
a found at index 16
a found at index 28
a found at index 32

Please enter the number of rows for the multiplication table: 12
   1
   2   4
   3   6   9
   4   8  12  16
   5  10  15  20  25
   and so on
"""

numRows = int(input("Please enter the number of rows for the multiplication table: "))

for row in range(1, numRows + 1):
    values = []
    for col in range(1, row + 1):
        values.append(str(row * col))

    # Create a right aligned format specifier string for list values
    fmt = "{:>5}" * len(values)

    # print the list with generated format specifier
    print(fmt.format(*values))

"""
Execution results:

a found at index 13
a found at index 16
a found at index 28
a found at index 32
Please enter the number of rows for the multiplication table: 12
    1
    2    4
    3    6    9
    4    8   12   16
    5   10   15   20   25
    6   12   18   24   30   36
    7   14   21   28   35   42   49
    8   16   24   32   40   48   56   64
    9   18   27   36   45   54   63   72   81
   10   20   30   40   50   60   70   80   90  100
   11   22   33   44   55   66   77   88   99  110  121
   12   24   36   48   60   72   84   96  108  120  132  144

"""
