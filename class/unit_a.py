"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit A in-class assignment
"""


def rectangle(height: float, width: float, floor: bool) -> None:
    if floor:
        height //= 2
        width //= 2

    area = width * height

    label = 'height:'
    print(f'{label:<10}{height}')

    label = 'width:'
    print(f'{label:<10}{width}')

    label = 'area:'
    print(f'{label:<10}{area}')


if __name__ == '__main__':
    rectangle(2.9, 7.1, False)
    print()
    rectangle(2.9, 7.1, True)


"""
height:   2.9
width:    7.1
area:     20.59

height:   1.0
width:    3.0
area:     3.0
"""
