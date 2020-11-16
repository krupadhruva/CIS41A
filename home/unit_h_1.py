"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit H take-home assignment
"""

import re

"""
First Script - Variable-Length Keyword Arguments - kwargs

This exercise develops and extends concepts introduced in the second script of the take-home lab F.

Here, we will be passing a variable number of keyword arguments to a function. You might recognize that the
terminology "variable number of keyword arguments" is just another way of describing a dictionary. In fact, this
is what we will be doing - passing a dictionary to a function and using certain of the key(word)
values - see functions (scroll down to the section called Arbitrary Number of Keyword Parameters).

For this exercise, imagine that there is a complex piece of equipment, perhaps a car or a spacecraft, and that all
of its various subsystems periodically send out status messages to be read and evaluated by an overseer system.
Each message contains just a small amount of data - perhaps only one or two keywords out of the hundreds of things
that overseer system must monitor.
However, we will restrict ourselves to only three things: temperature, CO2level, and miscError.

Write an overseerSystem function that has a kwargs argument.

Within the function, see if the keyword temperature exists in kwargs. If it does, and the temperature is greater than
500, print a warning with the temperature. 
Also see if the keyword CO2level exists in kwargs. If it does, and the CO2level is greater than .15, print a warning
with the CO2level. 
Lastly, see if the keyword miscError exists in kwargs. If it does, print a warning with the miscError number.

Test from main by creating five messages and calling the overseerSystem function with each message.

Message1 is temperature:550 
Message2 is temperature:475 
Message3 is temperature:450, miscError:404 
Message4 is CO2level:.18 
Message5 is CO2level:.2, miscError:418 

Sample Execution Results:

Warning: temperature is 550
Misc error #404
Warning: CO2level is 0.18
Warning: CO2level is 0.2
Misc error #418
"""


def overseerSystem(**kwargs):
    if "temperature" in kwargs:
        temperature = kwargs.get("temperature")
        if temperature > 500:
            print(f"Warning: temperature is {temperature}")

    if "CO2level" in kwargs:
        co2level = kwargs.get("CO2level")
        if co2level > 0.15:
            print(f"Warning: CO2level is {co2level}")

    if "miscError" in kwargs:
        print(f"Misc error #{kwargs.get('miscError')}")


def messageTokwargs(msg: str) -> {}:
    """Helper method to convert message with ':' separated key/value
    into dictionary to be used as kwargs

    The returned dictionary can be used as variable length
    keyword args in call to overseerSystem()
    """
    kwargs = {}

    # Split message string on space or comma as delimiter
    words = re.split("[ \t,]", msg)

    # Search for colon separated key/value pair to form kwargs
    for word in words:
        kv = word.partition(":")
        if kv[1] == ":":
            try:
                # If value is a number, store them as appropriate typed value
                kwargs[kv[0]] = int(kv[2]) if kv[2].isnumeric() else float(kv[2])
            except ValueError:
                kwargs[kv[0]] = kv[2]

    return kwargs


def main():
    # Direct invocation of overseerSystem() with keyword arguments
    """
    overseerSystem(temperature=550)
    overseerSystem(temperature=475)
    overseerSystem(temperature=450, miscError=404)
    overseerSystem(CO2level=0.18)
    overseerSystem(CO2level=0.2, miscError=418)
    """

    overseerSystem(**messageTokwargs("Message1 is temperature:550"))
    overseerSystem(**messageTokwargs("Message2 is temperature:475"))
    overseerSystem(**messageTokwargs("Message3 is temperature:450, miscError:404"))
    overseerSystem(**messageTokwargs("Message4 is CO2level:.18"))
    overseerSystem(**messageTokwargs("Message5 is CO2level:.2, miscError:418"))


if __name__ == "__main__":
    main()


"""
Execution results:

Warning: temperature is 550
Misc error #404
Warning: CO2level is 0.18
Warning: CO2level is 0.2
Misc error #418
"""
