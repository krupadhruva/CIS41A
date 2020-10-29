"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit E take-home assignment
"""

"""
Write a script that can determine where different plants can be planted.

Each plant has a name, a type (Flower, Vegetable, Tree, etc.), and a maximum height.
There are three gardens as follows:

The Vegetable Garden can have only Vegetables, and there is no maximum height.
The Low Garden can have only Flowers, and there is a maximum height of 3.
The High Garden can have only Flowers, and there is a maximum height of 6.
Print ONE line that identifies the one or more gardens that a given plant can be planted in. If a plant does not match the criteria for any of the gardens, then say so.

Test the script six times with the following test data:

Name: Lily, Type: Flower, Height 3
Name: Bonsai, Type: Tree, Height 2
Name: Carrots, Type: Vegetable, Height 1
Name: Corn, Type: Vegetable, Height 8
Name: Rose, Type: Flower, Height 5
Name: Sunflower, Type: Flower, Height 8
"""

# Dictionary of plant type with maximum height
# Height 0 implies no limits
# Contains a special entry with name of garden to simplify output
vegetable_garden = {
    "name": "Vegetable garden",
    "Vegetable": 0,
}

low_garden = {
    "name": "Low garden",
    "Flower": 3,
}

high_garden = {
    "name": "High garden",
    "Flower": 6,
}


def find_garden():
    name = input("Please enter the plant name: ")
    type = input("Please enter the plant type: ")
    height = int(input("Please enter the plant height: "))

    gardens = []
    for garden in [vegetable_garden, low_garden, high_garden]:
        if type in garden and (garden[type] == 0 or height <= garden[type]):
            gardens.append(garden["name"])

    if len(gardens) > 0:
        print(f'A {name} can be planted in the {" or the ".join(gardens)}.')
    else:
        print(f"A {name} cannot be planted in any garden.")


if __name__ == "__main__":
    for _ in range(6):
        find_garden()


"""
Execution results:

Please enter the plant name: Lily
Please enter the plant type: Flower
Please enter the plant height: 3
A Lily can be planted in the Low garden or the High garden.
Please enter the plant name: Bonsai
Please enter the plant type: Tree
Please enter the plant height: 2
A Bonsai cannot be planted in any garden.
Please enter the plant name: Carrots
Please enter the plant type: Vegetable
Please enter the plant height: 1
A Carrots can be planted in the Vegetable garden.
Please enter the plant name: Corn
Please enter the plant type: Vegetable
Please enter the plant height: 8
A Corn can be planted in the Vegetable garden.
Please enter the plant name: Rose
Please enter the plant type: Flower
Please enter the plant height: 5
A Rose can be planted in the High garden.
Please enter the plant name: Sunflower
Please enter the plant type: Flower
Please enter the plant height: 8
A Sunflower cannot be planted in any garden.

"""
