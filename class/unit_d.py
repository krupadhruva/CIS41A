"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit D in-class assignment
"""

"""
Write one script with three parts.

All print output should include descriptions as shown in the example output below.

1) Dictionary Basics:

Create a dictionary of fruit and desserts made from the fruit. The fruit should be the key and the dessert should be the value. Use these key value pairs: 
apple:sauce 
peach:cobbler 
carrot:cake 
strawberry:sorbet 
banana:cream pie 
Add the mango fruit to the dictionary. Its dessert is sticky rice.
Change the strawberry dessert to shortcake.
Carrot is not a fruit, so remove carrot from the dictionary.
Print the apple dessert.
See if a banana dessert exists.
See if a pear dessert exists.
Print the keys in the dessert dictionary.
Print the values in the dessert dictionary.
Print the key-value pairs in the dessert dictionary.
"""


fruit_dessert = {
    "apple": "sauce",
    "peach": "cobbler",
    "carrot": "cake",
    "strawberry": "sorbet",
    "banana": "cream pie",
}

fruit_dessert["mango"] = "sticky rice"

fruit_dessert["strawberry"] = "shortcake"

del fruit_dessert["carrot"]

print(f"apple dessert is: {fruit_dessert['apple']}")

print(f"banana dessert exists: {'banana' in fruit_dessert.keys()}")

print(f"pear dessert exists: {'pear' in fruit_dessert.keys()}")

print(fruit_dessert.keys())

print(fruit_dessert.values())

"""
2) Combining dictionaries:

Create a dictionary named capitols1 and populate it with these key value pairs: 
Alabama:Montgomery 
Alaska:Juneau 
Arizona:Phoenix 
Arkansas:Little Rock 
California:Sacramento 
Create a dictionary named capitols2 and populate it with these key value pairs: 
California:Sac. 
Colorado:Denver 
Connecticut:Hartford 
Be sure that the California capitol is Sac. and not Sacramento.
Using the dictionary update() method, update capitols1 with capitols2.
Print the sorted capitols (values). Note the updated value of California's capitol.
"""
print()

capitols1 = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
}

capitols2 = {"California": "Sac.", "Colorado": "Denver", "Connecticut": "Hartford"}

capitols1.update(capitols2)

print(f"Sorted state capitols: {sorted(capitols1.values())}")

"""
3) Sets Basics:

Create a set named class1 and populate it with the students Li, Audry, Jia, Migel, Tanya.
Create a set named class2 and populate it with the students Sasha, Migel, Tanya, Hiroto, Audry.
Add John to class1.
Print a sorted list of students who are in both classes.
Print a sorted list of all students.
Test to see if Sasha is in class1.
Sample Execution Results:

apple dessert is: sauce
banana dessert exists: True
pear dessert exists: False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])
dict_items([('apple', 'sauce'), ('peach', 'cobbler'), ('strawberry', 'shortcake'), ('banana', 'cream pie'), ('mango', 'sticky rice')])
Sorted state capitols: ['Denver', 'Hartford', 'Juneau', 'Little Rock', "Montgomery", 'Phoenix', 'Sac.']
Students in both classes: ['Audry', 'Migel', 'Tanya']
All students: ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
Sasha is in class1: False
"""

class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}

class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}

class1.add("John")

print(f"Students in both classes: {sorted(class1 & class2)}")

print(f"All students: {sorted(class1 | class2)}")

print(f"Sasha is in class1: {'Sasha' in class1}")

"""
Execution results:

apple dessert is: sauce
banana dessert exists: True
pear dessert exists: False
dict_keys(['apple', 'peach', 'strawberry', 'banana', 'mango'])
dict_values(['sauce', 'cobbler', 'shortcake', 'cream pie', 'sticky rice'])

Sorted state capitols: ['Denver', 'Hartford', 'Juneau', 'Little Rock', 'Montgomery', 'Phoenix', 'Sac.']
Students in both classes: ['Audry', 'Migel', 'Tanya']
All students: ['Audry', 'Hiroto', 'Jia', 'John', 'Li', 'Migel', 'Sasha', 'Tanya']
Sasha is in class1: False
"""
