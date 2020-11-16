"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit C take-home assignment
"""

"""
First Script - Working with Lists

All print output should include descriptions as shown in the example output below.

Create an empty list called list1
Populate list1 with the values 1,3,5
Create list2 and populate it with the values 1,2,3,4
Create list3 by using + (a plus sign) to combine list1 and list2. Print list3.
Use sequence operator in to test list3 to see if it contains a 3, print True/False result (do with one line of code).
Count the number of 3s in list3, print the result.
Determine the index of the first 3 in list3, print the result.
Pop this first 3 and assign it to a variable called first3, print first3.
Create list4, populate it with list3's sorted values, using the sorted built-in function.
Print list3 and list4.
Slice list3 to obtain a list of the values 1,2,3 from the middle of list3, print the result.
Determine the length of list3, print the result.
Determine the max value of list3, print the result.
Sort list3 (use the list sort method), print list3.
Create list5, a list of lists, using list1 and list2 as elements of list5, print list5.
Print the value 4 contained within list5.
Example output:

d) list3 is: [1, 3, 5, 1, 2, 3, 4]
e) list3 contains a 3: True
f) list3 contains 2 3s
g) The index of the first 3 contained in list3 is 1
h) first3 = 3
j) list3 is now: [1, 5, 1, 2, 3, 4]
j) list4 is: [1, 1, 2, 3, 4, 5]
k) Slice of list3 is: [1, 2, 3]
l) Length of list3 is 6
m) The max value in list3 is 5
n) Sorted list3 is: [1, 1, 2, 3, 4, 5]
o) list5 is: [[1, 3, 5], [1, 2, 3, 4]]
p) Value 4 from list5: 4
"""

list1 = []
list1.extend([1, 3, 5])

list2 = [1, 2, 3, 4]

list3 = list1 + list2
print(f"list3 is: {list3}")

print(f"list3 contains a 3: {3 in list3}")

print(f"list3 contains {list3.count(3)} 3s")

print(f"The index of the first 3 contained in list3 is {list3.index(3)}")

first3 = list3.pop(list3.index(3))
print(f"first3 = {first3}")

print(f"list3 is now: {list3}")

list4 = sorted(list3)
print(f"list4 is: {list4}")

print(f"Slice of list3 is: {list3[2:-1]}")

print(f"Length of list3 is {len(list3)}")

print(f"The max value in list3 is {max(list3)}")

list3.sort()
print(f"Sorted list3 is: {list3}")

list5 = [list1, list2]
print(f"list5 is: {list5}")

print(f"Value 4 from list5: {list5[1][3]}")


"""
Execution results:

list3 is: [1, 3, 5, 1, 2, 3, 4]
list3 contains a 3: True
list3 contains 2 3s
The index of the first 3 contained in list3 is 1
first3 = 3
list3 is now: [1, 5, 1, 2, 3, 4]
list4 is: [1, 1, 2, 3, 4, 5]
Slice of list3 is: [1, 2, 3]
Length of list3 is 6
The max value in list3 is 5
Sorted list3 is: [1, 1, 2, 3, 4, 5]
list5 is: [[1, 3, 5], [1, 2, 3, 4]]
Value 4 from list5: 4
"""
