"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit G take-home assignment
"""

"""
Part One - Reading a data file

For this exercise, you will need to download the file States.txt from Canvas and save it into the same directory as
your Python script. To do this, login to Canvas, select CIS 41A, select Files, select States.txt, select Download,
and save into the same directory with your unit G take-home Python script.

The file has 50 lines of data, one for each state in the Unites States. Each line of data contains three pieces of
data separated by a space: the two letter abbreviation of the state's name, the region that the state is in,
and the 2016 population of the state.

You need to find and print the state with the highest population in the Midwest region.

Example output:

Highest population state in the Midwest is: IL 12802000
"""


def build_population_distribution(filter_by_region=()):
    try:
        with open("States.txt", mode="r") as fh:
            state_population_map = {}
            for line in fh.readlines():
                entries = line.rstrip("\r\n").split(" ")

                # Apply filter if provided
                if len(filter_by_region) == 0 or entries[1] in filter_by_region:
                    state_population_map[entries[0]] = int(entries[2])

            return state_population_map
    except IndexError:
        print("error in data, insufficient fields")
    except OSError as ex:
        print(f"error opening file for read: {ex}")


"""
Part Two - A Dictionary of Lists

Download the file USPresidents.txt from from Canvas and save it into the same directory as your Python script.
To do this, login to Canvas, select CIS 41A, select Files, select USPresidents.txt, select Download, and save
into the same directory with your unit G take-home Python script.

The file has 44 lines of data, one for each president in the history of the Unites States. Each line of data contains
two pieces of data separated by a space: the two letter abbreviation of the name of the state where the president
was born, and the name of the president (for your convenience, the president's name has been converted to a
single string - George Washington has been converted to George_Washington).

Using the data from the file, you need to build a dictionary of states and the presidents born in those states.
Each key will be a state abbreviation and each value will be a list of presidents.

After building the dictionary, determine the state with the most presidents and how many presidents were born there.
Print their names.

Example output:

The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
And so on...
"""


def build_us_presidents_map():
    """
    Reads a file with president's birth state and president name

    returns: Dictionary of state abbrev and presidents born in the state
    """
    try:
        with open("USPresidents.txt", mode="r") as fh:
            # Map of state and presidents
            state_presidents = {}

            for line in fh.readlines():
                # Default split is on any white space (space or tab)
                entries = line.rstrip("\r\n").split()

                # Insert new entry or append to existing entry
                if entries[0] in state_presidents:
                    state_presidents[entries[0]].append(entries[1])
                else:
                    state_presidents[entries[0]] = [entries[1]]

            return state_presidents
    except IndexError as ex:
        print(f"error in data, insufficient fields: {line}, {ex}")
    except OSError as ex:
        print(f"error opening file for read: {ex}")


"""
Part Three - Dictionary Keys and Sets

Build a second dictionary from the USPresidents.txt file described in the previous exercise. Each key will again be
a state abbreviation, however, the value will be the count of presidents from that state.

Create a set of the ten most populous US states (CA, TX, FL, NY, IL, PA, OH, GA, NC, MI).

Then create a new set that represents a set of populous US states that have had presidents born in them (you should
be able to do this with one line of code).

Print a count of this new set along with an alpha-sorted listing of these states and how many presidents have been
born in them.

Example output:

8 of the 10 high population states have had presidents born in them:
CA 1
GA 1
IL 1
NC 2 
And so on...
"""


def main():
    # Part 1

    # Filter states that are part of Midwest
    midwest_population_map = build_population_distribution(filter_by_region=["Midwest"])

    # Get the state with highest population
    result = max(midwest_population_map.items(), key=lambda item: item[1])
    print(f"Highest population state in the Midwest is: {result[0]} {result[1]}")

    # Part 2
    print()
    state_presidents_map = build_us_presidents_map()
    state_with_max_presidents = max(
        state_presidents_map.items(), key=lambda item: len(item[1])
    )
    print(
        f"The state with the most presidents is {state_with_max_presidents[0]} with {len(state_with_max_presidents[1])} presidents:"
    )
    print("\n".join(state_presidents_map[state_with_max_presidents[0]]))

    # Part 3
    print()
    state_presidents_count = {k: len(v) for (k, v) in state_presidents_map.items()}
    population_map = build_population_distribution()
    top_10_populous_states = set(
        sorted(population_map, key=population_map.get, reverse=True)[:10]
    )

    populous_states_with_presidents = top_10_populous_states & set(
        state_presidents_map.keys()
    )

    for state in sorted(populous_states_with_presidents):
        print(f"{state} {state_presidents_count.get(state)}")


if __name__ == "__main__":
    main()


"""
Execution results:

Highest population state in the Midwest is: IL 12802000

The state with the most presidents is VA with 8 presidents:
George_Washington
James_Madison
James_Monroe
John_Tyler
Thomas_Jefferson
William_Henry_Harrison
Woodrow_Wilson
Zachary_Taylor

CA 1
GA 1
IL 1
NC 2
NY 5
OH 7
PA 1
TX 2
"""
