"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit H take-home assignment
"""

"""
We will be building a BritCoins class that allows you to work with British money as it was denominated up to 1971 - see: Old English Money. While there were a variety of types of coins, we will only be concerned with pounds, shillings, and pennies. A shilling was worth 12 pennies, and a pound was worth 20 shillings. Therefore, a pound was worth 240 pennies.

The class will allow you to initialize a BritCoins object with any given amount of pounds, shillings and pennies, add and subtract BritCoins objects, and to print a string that represents the value of the coins used to initialize a BritCoins object.

Certain aspects of the BritCoins class will parallel the Length class example shown here: magic methods (scroll down to the Example class: Length section). However, there will be some significant differences.

The idea of the BritCoins class is that you will pass the class a dictionary of coinTypes (keys) and the quantities of each coinType (values). In other words, we will be using kwargs as we did in the third exercise of the Lab H Takehome. The class will then calculate how many pennies these coins represent and save this totalPennies value. The totalPennies value will later be used for addition and subtraction as well as for generating the coin value string.

Building the class:

Create a BritCoins class with the following methods: __init__, __add__ , __sub__ , __str__. There will also be a private class dictionary called __coinValues as follows (this is similar to the __metric variable in the Length example).

__coinValues = {"pound":240, "shilling":12, "penny":1} #value of each type of coin in pennies

The __init__ method should have the parameters self, and **kwargs. Start by initializing a self.totalPennies attribute to zero. Then iterate through the kwargs. For each coinType in kwargs, add the value in pennies of that type and quantity of coin to a self.totalPennies. Determine this value by multiplying the number of coins (get this from kwargs) by the coin value (get this from __coinValues - do not hardcode the values!). As an example, if init receives 4 pound, 3 shilling and 2 penny, totalPennies should be 998 (4*240+3*12+2*1).

The __add__ method should have the parameters self and other. Calculate a local total by adding self.totalPennies to other.totalPennies. Then return this value. However, there are two crucial considerations here. The first is that when we add two BritCoins objects, the result of this addition should also be a BritCoins object. Therefore, what we want to return isn't the total, but is instead a new BritCoins object that has been initialized with the appropriate coinage. So, we need to create and return an instance of the class. We can do this within the class itself! The second consideration is that when we create this instance, we need to provide an appropriate argument for BritCoins. We can't just pass the total (of say, 998) - we need to pass a dictionary like {"penny":998}. Further, we need to use appropriate notation when making this BritCoins call (as you did when testing the overseerSystem function in the Lab H Takehome).

The __sub__ method should have the parameters self and other. It is similar to the add method except that you subtract other from self instead of adding it.

The __str__ method has the parameter self and should return a string that represents the value of the BritCoins object. The string should be formatted as shown below, showing pounds, shillings and pennies. From self.totalPennies, you will need to calculate how many of each coin type there are using floor division or some other technique. Note that this string representation won't necessarily be the coins used to initialize the BritCoins object - it will be the value of the BritCoins object. For example, if the BritCoins object was initialized with 25 shillings, the return should be 1 pounds 5 shillings 0 pennies.

For this script, the test code should be after your class code – don't worry about calling from main.

Test the BritCoins class with the following data:

c1 = 4 pound, 24 shilling, 3 penny 
c2 = 3 pound, 4 shilling, 5 penny 
c3 = c1 + c2 
c4 = c1 - c2

Then print c1, c2, c3 and c4.
"""


class BritCoins:
    # Conversion map
    __coinValues = {"pound": 240, "shilling": 12, "penny": 1}

    # For string representation: Handles plural form based on count
    __pluralForm = {"pound": "pounds", "shilling": "shillings", "penny": "pennies"}

    def __init__(self, **kwargs):
        # Evaluate only keywords that we are interested in and perform conversion
        self.totalPennies = sum(
            (
                BritCoins.__coinValues[coin] * kwargs[coin]
                for coin in set(BritCoins.__coinValues) & set(kwargs)
            )
        )

    def __add__(self, other):
        result = BritCoins()
        result.totalPennies = self.totalPennies + other.totalPennies
        return result

    def __sub__(self, other):
        result = BritCoins()
        result.totalPennies = self.totalPennies - other.totalPennies
        return result

    def __str__(self):
        remaining = self.totalPennies
        results = []

        # Convert starting from the highest conversion value to lowest
        for k, v in sorted(
            BritCoins.__coinValues.items(), key=lambda k: k[1], reverse=True
        ):
            count = remaining // v
            currency = k if count == 1 else BritCoins.__pluralForm[k]
            remaining -= count * v
            results.append(f"{count} {currency}")

        return ", ".join(results)


if __name__ == "__main__":
    c1 = BritCoins(pound=4, shilling=24, penny=3)
    c2 = BritCoins(pound=3, shilling=4, penny=5)
    c3 = c1 + c2
    c4 = c1 - c2

    print(c1)
    print(c2)
    print(c3)
    print(c4)


"""
Execution results:

5 pounds, 4 shillings, 3 pennies
3 pounds, 4 shillings, 5 pennies
8 pounds, 8 shillings, 8 pennies
1 pound, 19 shillings, 10 pennies
"""
