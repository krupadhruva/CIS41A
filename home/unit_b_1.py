"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit B take-home assignment
"""


from typing import Optional

# Based on the longest label we print
pad = 50
separator = ":"


def output(prefix: str, data: object, padding: Optional[int] = None) -> None:
    """
    Helper method to formatted print results
    @param prefix: Label or message prefix
    @param data: Value or result
    @param padding: Optional pad
    """
    global separator

    if padding is None:
        global pad
        padding = pad

    print(f"{prefix + separator:<{padding}}{data}")


"""
First Script - Working with Strings

This script contains four parts.
"""

"""
String Type Tests

Ask the user for a string (test with "ABC123").
Use method isupper to test the string, print the result.
Use method isdigit to test the string, print the result.
Use method isalpha to test the string, print the result.
"""

entry = input("Enter a string: ")

val = entry.isupper()
label = "isupper to test the string"
output(label, val)

val = entry.isdigit()
label = "isdigit to test the string"
output(label, val)

val = entry.isalpha()
label = "isalpha to test the string"
output(label, val)

"""
Escape Characters within a string
Use newline escape characters within a line of haiku

Assign the text "Type, type, type away. Compile. Run. Hip hip hooray! No error today!" to a single variable (be sure to add newline escape characters). This should be done in a single line of code.
Print, so that the output appears as follows:

Type, type, type away.
Compile. Run. Hip hip hooray!
No error today!
      
Haiku by Samantha W.
"""
print()

val = "Type, type, type away.\nCompile. Run. Hip hip hooray!\nNo error today!\n"
print(f"{val}\nHaiku by Samantha W.")


"""
Slicing a string

Assign the text "And now for something completely different" to a variable called quote.
Slice quote to obtain the text "And no" from the beginning of the quote, print the results.
Slice quote to obtain the text "rent" from the end of the quote, print the results.
Slice quote to obtain the text "me" from the middle of the quote, print the results.
Slice quote to obtain the text "Adnwf..." by extracting every other letter, print the results.
Slice quote to obtain the text "tnere..." by reversing the quote, print the results.
"""
pad = 75
print()

quote = "And now for something completely different"

idx = quote.index("w")
label = 'obtain the text "And no" from the beginning of the quote'
val = quote[:idx]
output(label, val)

idx = quote.rindex("r")
label = 'obtain the text "rent" from the end of the quote'
val = quote[idx:]
output(label, val)

idx1 = quote.index("m")
idx2 = quote.index("e")
label = 'obtain the text "me" from the middle of the quote'
val = quote[idx1 : idx2 + 1]
output(label, val)

label = 'obtain the text "Adnwf..." by extracting every other letter'
val = quote[::2]
output(label, val)

label = 'obtain the text "tnere..." by reversing the quote'
val = quote[::-1]
output(label, val)


"""
Using string operators + and *

Assign the text ".~*'" to a variable called pattern1.
Create a variable called pattern2, assign to it pattern1 combined with pattern1 reversed. pattern2 should now contain the string ".~*''*~."
Print pattern2 repeated five times. The output should appear as follows:
.~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.
"""
print()

pattern1 = ".~*'"
pattern2 = pattern1 + pattern1[::-1]
val = pattern2 * 5
label = "pattern2 repeated five times"
output(label, val)


""" 
Execution results: 

Enter a string: ABC123
isupper to test the string:                       True
isdigit to test the string:                       False
isalpha to test the string:                       False

Type, type, type away.
Compile. Run. Hip hip hooray!
No error today!

Haiku by Samantha W.

obtain the text "And no" from the beginning of the quote:                  And no
obtain the text "rent" from the end of the quote:                          rent
obtain the text "me" from the middle of the quote:                         me
obtain the text "Adnwf..." by extracting every other letter:               Adnwfrsmtigcmltl ifrn
obtain the text "tnere..." by reversing the quote:                         tnereffid yletelpmoc gnihtemos rof won dnA

pattern2 repeated five times:                                              .~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.
"""
