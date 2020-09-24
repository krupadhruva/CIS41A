"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit B in-class assignment
"""

# Based on the longest label we print
pad = 50
separator = ':'

'''
String methods

Ask the user for a name (test with George Washington).
Print the name in all uppercase letters.
Print the length of the name.
Print the 4th character of the name (r).
Create a variable called name2. Assign to name2 the name with all "o" characters replaced with "x"s.
Print name2.
Print the original name.
'''

entry = input('Enter a name: ')

val = entry.upper()
label = 'name in all uppercase letters'
print(f'{label+separator:<{pad}}{val}')

label = 'length of the name'
val = len(entry)
print(f'{label+separator:<{pad}}{val}')

label = '4th character of the name'
if len(entry) >= 4:
    val = entry[3]
    print(f'{label + separator:<{pad}}{val}')

name2 = entry.replace("o", "x")
label = 'name with all "o" characters replaced with "x"s'
print(f'{label + separator:<{pad}}{name2}')

'''
Counting and Finding

Assign the text "Believe you can and you're halfway there." to a variable called quote (this is a quote from Theodore Roosevelt).
Count how many "a" characters there are, print the result.
Print the index of all the "a" characters. 
Hint: Except for the first find, set the start location for the next find as the previous location found index + 1. The second argument in the find method is the index where the find starts looking. 
A fuller explanation of the find method is given in string-methods
'''
print()

quote = "Believe you can and you're halfway there."

label = 'Count how many "a" characters there are'
print(f'{label + separator:<{pad}}{quote.count("a")}')

label = 'index of all the "a" characters'
indices = ""
try:
    offset = 0
    while offset < len(quote):
        idx = quote.index("a", offset)
        if offset == 0:
            indices = str(idx)
        else:
            indices = indices + ", " + str(idx)

        offset = idx + 1
except ValueError:
    pass
finally:
    print(f'{label + separator:<{pad}}{indices}')

'''
Execution results:

Enter a name: George Washington
name in all uppercase letters:                    GEORGE WASHINGTON
length of the name:                               17
4th character of the name:                        r
name with all "o" characters replaced with "x"s:  Gexrge Washingtxn

Count how many "a" characters there are:          4
index of all the "a" characters:                  13, 16, 28, 32
'''
