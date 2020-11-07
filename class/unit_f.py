"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit F in-class assignment
"""

"""
Part One – Using a main function, Docstrings

Write a function called hello. The function has no arguments and no return value.
It simply prints the text "Hello World". Include a docstring that describes the function.

Write a main function, as described by the Python main function reading.
Call main, as described by the Python main function reading.
From main, call hello and then print hello’s docstring.
"""


def hello():
    """hello()
    This function prints Hello World"""
    print("Hello World")


"""
Part Two – Error Handling

Write a function called printListElement. The function has two arguments and no return value. The first argument is a list, and the second argument is a list index. The function will print an element from the list as determined by the list index. If the list index is invalid, print an error message.

We could accomplish this with a logic test, but instead, we will manage this with error handling.

Write a try block that attempts to print the list element. Catch any errors with an except block, print an error message.

From main, create a myList list with elements 0, 1, 2 by using the list and range commands.

Then, call printListElement with your list and a list index value of 3.
"""


def printListElement(data, index):
    try:
        print(f"Value at index={index}: {data[index]}")
    except IndexError:
        print("Error: bad index number.")


"""
Part Three – How Python function arguments are treated

There can be some confusion as to how Python functions treat their arguments - is it by reference or by value? Explore this for yourself.

From main, create a myInt variable and give it the value 3. Also create a myList list with elements 0, 1, 2.

Print the IDs of myInt and myList. Also print the ID of the last element of myList.

Now create a function called byVal which has one argument. In the function, add 7 to the argument. Print the ID of the argument before and after the change.

Create a second function called byRef which has one argument. In the function, add 7 to the last element in the list. Print the ID of the argument and the ID of the last element of the argument before and after the change.

Now call byVal with myInt and then call byRef with myList. Next, again print the IDs of MyInt, myList, and the last element of myList. Finally, print myInt and MyList from main. Can you explain the results?
"""


def byVal(data):
    print(f"Original ID of parameter in byVal {id(data)}")
    data += 7
    print(f"ID of parameter in byVal after change {id(data)}")


def byRef(data):
    print(f"Original ID of parameter in byRef {id(data)}")
    print(f"Original ID of parameter's last element in byRef {id(data[-1])}")
    data[-1] += 7
    print(f"ID of parameter in byRef after change {id(data)}")
    print(f"ID of parameter's last element in byRef after change {id(data[-1])}")


def main():
    # Part 1
    hello()
    print(f"Help on function hello in module __main__:\n\n{hello.__doc__}")

    # Part 2
    print()
    myList = [*range(3)]
    printListElement(myList, 3)

    # Part 3
    print()

    myInt = 3
    print(f"Original ID of myInt in main is {id(myInt)}")
    print(f"Original ID of myList in main is {id(myList)}")
    print(f"Original ID of myList's last element in main is {id(myList[-1])}")

    byVal(7)
    byRef([*range(3)])

    byVal(myInt)
    byRef(myList)

    print(f"myInt is now: {myInt}")
    print(f"myList is now: {myList}")


if __name__ == "__main__":
    main()

"""
Can you explain the results?

* Variables of builtin types are immutable: Operations on builtin types result in new objects
  val and val += 7 results in 2 different id. '+' does not update the original object, it creates a new
  object and assigns val to the new object (which is the result of adding 7 to original value in val)
  
  The same happens when adding to a list element
  list[-1] and list[-1] += 7 results in 2 different id since the '+' operation is on builtin type

* Constructing a list with [*range(3)] multiple times resulted in list object with same ID.
  Could this be due to Python reusing the same returned result of call to 'range' since input has not changed?
  Searching on internet pointed to potential 'memoization', which is an optimization to reuse results of previous
  computation if input has not changed.
  
* Invoking function with built in data types like int is by value: The id changes between the callee and caller
* Invoking functions with collections like list is by reference: The id remains same across callee and caller

* Modifications done to values passed by reference is seen both in callee and caller
"""

"""
Execution results:

Hello World
Help on function hello in module __main__:

hello()
    This function prints Hello World

Error: bad index number.

Original ID of myInt in main is 4299872624
Original ID of myList in main is 4302116992
Original ID of myList's last element in main is 4299872592
Original ID of parameter in byVal 4299872752
ID of parameter in byVal after change 4299872976
Original ID of parameter in byRef 4302091840
Original ID of parameter's last element in byRef 4299872592
ID of parameter in byRef after change 4302091840
ID of parameter's last element in byRef after change 4299872816
Original ID of parameter in byVal 4299872624
ID of parameter in byVal after change 4299872848
Original ID of parameter in byRef 4302116992
Original ID of parameter's last element in byRef 4299872592
ID of parameter in byRef after change 4302116992
ID of parameter's last element in byRef after change 4299872816
myInt is now: 3
myList is now: [0, 1, 9]
"""
