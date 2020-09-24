"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit D take-home assignment
"""

from collections import namedtuple


"""
Part One - Sets

Create a set named class1 and populate it with the students Li, Audry, Jia, Migel, Tanya.
Create a set named class2 and populate it with the students Sasha, Migel, Tanya, Hiroto, Audry.
Create a set named class3 and populate it with the students Migel, Zhang, Hiroto, Anita, Jia.
Print a sorted list of students who are in all three classes.
Print a sorted list of all students.
Print a sorted list of all students in class1 but not class2 or class3.
"""

class1 = {"Li", "Audry", "Jia", "Migel", "Tanya"}
class2 = {"Sasha", "Migel", "Tanya", "Hiroto", "Audry"}
class3 = {"Migel", "Zhang", "Hiroto", "Anita", "Jia"}

print(f"Students in all three classes: {sorted(class1 & class2 & class3)}")

print(f"All students: {sorted(class1 | class2 | class3)}")

print(
    f"Students in class1 but not class2 or class3: {sorted(class1.difference((class2 | class3)))}"
)

"""
Part Two - Swap

Create a list containing elements 1, 2, 3
Swap the second and third elements of the list. Do this with one line of code.
Print the list.
"""
print()

list1 = [1, 2, 3]
list1[2], list1[1] = list1[1], list1[2]
print(f"List after swap: {list1}")

"""
Part Three – Tuple Basics

For Parts Three, Four and Five, you will be working with data about the movie Casablanca.

Create a tuple that contains the elements Casablanca, 1942, romantic drama.
Unpack the tuple into variables title, year, genre.
Print the title.
"""
print()

movie = ("Casablanca", 1942, "romantic drama")
title, year, genre = movie

print(f"My favorite movie is: {title}")

"""
Part Four – Named Tuple

Define a named tuple called Movie that contains the fields title, year, genre.
Create a Movie tuple that contains the elements Casablanca, 1942, romantic drama.
Print the title.
"""
print()

Movie = namedtuple("Movie", "title year genre")
movie = Movie(title="Casablanca", year=1942, genre="romantic drama")

print(f"My favorite movie is: {movie.title}")

"""
Part Five – Named Tuple Containing a List

Define a named tuple called Moviestars that contains the fields title, year, genre, stars.
Create a Moviestars tuple called favoritemovie that contains the elements Casablanca, 1942, romantic drama, and a list containing elements Humphrey Bogart, Ingrid Bergman.
Append Claude Rains to the stars list. Hint: Use the syntax favoritemovie.stars.append
Print star Ingrid Bergman.
Print favoritemovie.
Note that, even though a tuple is immutable, we are able to change a list that is contained by a tuple.
"""
print()

Moviestars = namedtuple("Moviestars", "title, year, genre, stars")
favoritemovie = Moviestars(
    "Casablanca", 1942, "romantic drama", ["Humphrey Bogart", "Ingrid Bergman"]
)
favoritemovie.stars.append("Claude Rains")

print(f"My favorite star is: {favoritemovie.stars[1]}")

print(favoritemovie)

""" 
Execution results:
 
Students in all three classes: ['Migel']
All students: ['Anita', 'Audry', 'Hiroto', 'Jia', 'Li', 'Migel', 'Sasha', 'Tanya', 'Zhang']
Students in class1 but not class2 or class3: ['Li']

List after swap: [1, 3, 2]

My favorite movie is: Casablanca

My favorite movie is: Casablanca

My favorite star is: Ingrid Bergman
Moviestars(title='Casablanca', year=1942, genre='romantic drama', stars=['Humphrey Bogart', 'Ingrid Bergman', 'Claude Rains']) 
"""
