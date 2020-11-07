"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit F take-home assignment
"""

"""
Part One – Keyword Arguments and Default Values

Write an invoice function. 
The function will generate a simple invoice and will have two required arguments and two keyword arguments. 
The two required arguments are unitPrice and quantity. 
The first keyword argument is shipping, and it has a default value of 10. 
The second keyword argument is handling, and it has a default value of 5. 

Test it twice from main: 
First test: unitPrice 20, quantity 4, and shipping 8 (handling is not specified). 
Second test: unitPrice 15, quantity 3, and handling 15 (shipping is not specified). 
Don't worry about making the formatting pretty. 
"""


def invoice(unitPrice, quantity, shipping=10, handling=5):
    print(f"Cost (unitPrice x quantity) = {unitPrice * quantity}")
    print(f"Shipping = {shipping}")
    print(f"Handling = {handling}")
    print(f"Total = {(unitPrice * quantity) + shipping + handling}")


"""
Part Two – args (Variable-Length Arguments)

Write a printGroupMembers function. 
The function prints a list of students who are working together on a group project, as well as the group name. 
The function has one required argument, the group name, and one variable-length argument that contains the student names. 

Test it twice from main: 
First test: Call as follows: 
printGroupMembers("Group A", "Li", "Audry", "Jia") 
Second test: Create a list as follows: 
groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"] 
and then call the function using this list. 
"""


def printGroupMembers(groupName, *students):
    print(f"Members of {groupName}")
    print("\n".join(students))


"""
Part Three – Non-Rectangular (Ragged) 2D lists

Write two functions that will build and display a Bell triangle - see: What is a Bell triangle 

A Bell triangle can be constructed as follows:

The first row has a single element which has the value 1.
For the second row and all subsequent rows:
The number of elements in a row is equal to the number of elements in the previous row + 1.
The first element in the row is equal to the last element of the previous row.
The second through nth elements of a row are calculated by adding the value of the previous element (n-1) in the current row to the (n-1) element of the previous row.
As an example of this calculation, start by looking at the triangle shown below. To calculate the 3rd (n=3) element of the 4th row, we add the 2nd (3-1=2) element of the 4th row (7) to the 2nd (3-1=2) element of the 3rd row (3), with the total being 10 (7+3=10).

The first function should be called buildBell. It has one argument, the number of rows, and returns a ragged table (a list of lists).

The second function should be called printBell. It has one argument, a ragged table (a list of lists). Generate formatted output where each number is right justified within a fixed field size, so that the numbers in each column are aligned.

Hint: The easiest way to format the numbers is probably by using the rjust string function.

Test by calling buildBell from main to build a Bell triangle with 8 rows.

Then call printBell from main to print the triangle.
"""


def buildBell(rows):
    if rows == 0:
        return []

    bell_table = [[1]]
    for _ in range(rows - 1):
        last_row = bell_table[-1]
        row = [last_row[-1]]
        for val in last_row:
            row.append(val + row[-1])

        bell_table.append(row)

    return bell_table


def printBell(bell_table):
    for row in bell_table:
        print()
        for val in row:
            print(str(val).rjust(5, " "), end="")


if __name__ == "__main__":
    invoice(20, 4, shipping=8)
    print()
    invoice(15, 3, handling=15)

    print()
    printGroupMembers("Group A", "Li", "Audry", "Jia")

    groupB = ["Group B", "Sasha", "Migel", "Tanya", "Hiroto"]
    printGroupMembers(*groupB)

    table = buildBell(8)
    printBell(table)


"""
Execution results:

Cost (unitPrice x quantity) = 80
Shipping = 8
Handling = 5
Total = 93

Cost (unitPrice x quantity) = 45
Shipping = 10
Handling = 15
Total = 70

Members of Group A
Li
Audry
Jia
Members of Group B
Sasha
Migel
Tanya
Hiroto

    1
    1    2
    2    3    5
    5    7   10   15
   15   20   27   37   52
   52   67   87  114  151  203
  203  255  322  409  523  674  877
  877 1080 1335 1657 2066 2589 3263 4140
"""
