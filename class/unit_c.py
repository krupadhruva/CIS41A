"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit C in-class assignment
"""


"""
List script

After you finish the quiz and turn it in, write the following script.

All print output should include descriptions as shown in the example output below.

Create a list called list1 that has elements 2, 4.1, 'hello'.
Copy list1 to list2 so that list2 is an alias of list1 (shallow copy).
Copy list1 to list3 so that list3 is a new list (true deep copy).
Using ==, compare list1 to list2, list 1 to list 3, and list 2 to list3.
Using is, compare list1 to list2, list 1 to list 3, and list 2 to list3.
Print the ids of list 1, list2, and list3.
Append a new element with value 8 to list1.
After the first element of list2, insert an element 'goodbye'.
Remove the first element from list3.
Print each of the three lists. Do the results match what you expected?
Tell the instructor what these results mean.
Example output:

list1 == list2: ...
list1 == list3: ...
list2 == list3: ...
list1 is list2: ...
list1 is list3: ...
list2 is list3: ...
list1 ID: ...
list2 ID: ...
list3 ID: ...
list1 printed: ...
list2 printed: ...
list3 printed: ...
"""

list1 = [2, 4.1, "hello"]
list2 = list1.copy()
list3 = list1[:]

# Using copy package
# import copy
# list2 = copy.copy(list1)
# list3 = copy.deepcopy(list1)

print(f"list1 == list2: {list1 == list2}")
print(f"list1 == list3: {list1 == list3}")
print(f"list2 == list3: {list2 == list3}")

print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")
print(f"list2 is list3: {list2 is list3}")

print(f"list1 ID: {id(list1)}")
print(f"list2 ID: {id(list2)}")
print(f"list3 ID: {id(list3)}")

list1.append(8)
list2.insert(1, "goodbye")
list3.pop(0)

print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"list3: {list3}")

"""
Execution results:

list1 == list2: True
list1 == list3: True
list2 == list3: True
list1 is list2: False
list1 is list3: False
list2 is list3: False
list1 ID: 4382747328
list2 ID: 4382944128
list3 ID: 4382936768
list1: [2, 4.1, 'hello', 8]
list2: [2, 'goodbye', 4.1, 'hello']
list3: [4.1, 'hello']
"""
