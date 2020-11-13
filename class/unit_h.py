"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit H in-class assignment
"""

"""
Part 1 - A Basic Class - State Data

Create a StateData class with the following methods: __init__, __str__, displayState.
Note: __ is two underline characters.

The __init__ method should have the parameters self, name, abbreviation, region, and population and should store the name, abbreviation, region, and population as attributes.

The __str__ method has the parameter self and should return the state's name.

The displayState method has the parameter self and should print formatted state data as shown below.

Test the class by creating an instance of the class (instantiating) called s1 with the following data: "California", "CA", "West", 39250000. Print your state object (this will call the __str__ method). Then call displayState. This test code should be after your class code - don't worry about calling from main.

Sample Execution Results:

California
California (CA) is in the West region and has population of 39250000
"""


class StateData:
    def __init__(self, name, abbreviation, region, population):
        self.name = name
        self.addreviation = abbreviation
        self.region = region
        self.population = population

    def __str__(self):
        return self.name

    def displayState(self):
        print(
            f"{str(self.name)} ({self.addreviation}) is in the {self.region} region and has population of {self.population}"
        )


"""
Part 2 - Different ways of working with Attributes

Here we explore different ways to work with Python attributes. Note that, while one of the approaches we are using is set/get, this approach is generally deprecated in favor of the simpler dot notation.

Create a StateData2 class with the following methods: __init__, setRegion, getRegion.

The __init__ method should have the parameters self, name and should store the name as an attribute.

The setRegion should have the parameters self, region and should store the region as an attribute.

The getRegion should have the the parameter self and should return the the value of the region data variable.

Test the class by creating an instance of the class called s2 with the following data: "California". Then call setRegion with the argument "West". Then set the population attribute with the following line of code: s2.pop = 39250000

Then print four lines: s2.name, s2.getRegion(), s2.region, s2.pop

Again, this test code should be after your class code.

Sample Execution Results:

California
West
West
39250000
"""


class StateData2:
    pass

    def __init__(self, name):
        self.name = name

    def setRegion(self, region):
        self.region = region

    def getRegion(self):
        return self.region


"""
Part 3 - Data Hiding

Data hiding within Python is achieved with the use of special naming conventions: beginning an attribute name with either a single underscore (protected) or a double underscore (private).

Create a StateData2 class with the following method: __init__.

The __init__ method should have the parameter self. It should store the value "Public" in an attribute called public, the value " Protected" in an attribute called _protected (use a single underscore), and the value " Private" in an attribute called __private (use a double underscore).

Test the class by creating an instance of the class called test.

Try to print three lines: test.public, test._protected, test.__private
"""


class StateData3:
    """Since there is already a class named StateData2, creating StateData3"""

    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"


if __name__ == "__main__":
    # Part 1
    s1 = StateData("California", "CA", "West", 39250000)
    print(s1)
    s1.displayState()

    # Part 2
    print()
    s2 = StateData2("California")
    s2.setRegion("West")
    s2.pop = 39250000

    print(s2.name)
    print(s2.getRegion())
    print(s2.region)
    print(s2.pop)

    # Part 3
    print()
    test = StateData3()
    print(test.public)
    print(test._protected)
    print(test.__private)


"""
Execution results:

California
California (CA) is in the West region and has population of 39250000

California
West
West
39250000

Public
Protected
Traceback (most recent call last):
  File "/Users/krupadhruva/git/CIS41A/class/unit_h.py", line 131, in <module>
    print(test.__private)
AttributeError: 'StateData3' object has no attribute '__private'
"""
