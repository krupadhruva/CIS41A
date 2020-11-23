"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit I in-class assignment
"""

import math

"""
Part 1 of 1 - Basic Inheritance - Circle & Cylinder

You will be creating a Circle base (parent) class and a Cylinder class that inherits from it (child). 
Both classes and the code to test the classes will be contained within a single script.

The Circle class has the following methods: __init__, getArea. 
Circle's __init__ method should have the parameters self and radius, and should store the radius as an attribute. 
The getArea method has the parameter self and should return the circle's area (use the pi constant from the math module
when calculating the area).

The Cylinder class inherits from the Circle class and has the following methods: __init__, getVolume. 
Cylinder's __init__ method should have the parameters self, radius and height. From within Cylinder's __init__,
call Circle's __init__ to store the radius. The height should be stored as an attribute of the Cylinder. 
The getVolume method has the parameter self and should use the getArea method and calculate and return the
cylinder's volume. See: volume of a cylinder

Test by creating an instance of the Circle class with a radius of 4. Print the area of the circle, rounded to 2 places. 
Then, create an instance of the Cylinder class with a radius of 2 and a height of 5. Print the volume of the cylinder,
rounded to 2 places.

Sample Execution Results:

Circle area is: 50.27
Cylinder volume is: 62.83
"""


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def getArea(self):
        return math.pi * pow(self.radius, 2)


class Cylinder(Circle):
    def __init__(self, radius: float, height: float):
        self.height = height
        super(Cylinder, self).__init__(radius)

    def getArea(self):
        return 2 * (
            super(Cylinder, self).getArea() + (math.pi * self.radius * self.height)
        )

    def getVolume(self):
        return super(Cylinder, self).getArea() * self.height


if __name__ == "__main__":
    circle = Circle(4)
    cylinder = Cylinder(radius=2, height=5)

    print(f"Circle area is: {circle.getArea():.2f}")
    print(f"Cylinder volume is: {cylinder.getVolume():.2f}")


"""
Execution results:

Circle area is: 50.27
Cylinder volume is: 62.83
"""
