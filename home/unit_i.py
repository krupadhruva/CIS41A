"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit I take-home assignment
"""

"""
Part 1 of 1 - Inheritance with Multiple Children

We will be building a suite of three classes to manage library patrons and the books that they check out
(a library patron is someone who has a library account). 
All three classes and the code to test the classes will be contained within a single script.

The library has two types of patrons, adult and juvenile, and two types of books, adult and juvenile.
Juvenile patrons can only check out juvenile books, while adult patrons can check out any type of book.
Additionally, juvenile patrons have a limit of 2 books that they may have checked out at one time, while
adult patrons have a limit of 4 books that they may have checked out at one time.

We will write three classes: a parent LibraryPatron class, and AdultPatron and JuvenilePatron child classes.
Ideally, we would also have a Book class, but we will simplify things here by making a book be a list with
two elements: the title, and the book type - adult or juvenile (see the testing code below).
"""

"""
LibraryPatron class:

The LibraryPatron class has the following four methods: __init__, checkOutBook, returnBook, and printCheckedOutBooks.

The __init__ method should have the parameters self and name, and should store the name as an attribute (name is the
name of the patron). There should also be an additional attribute called booksCheckedOut which should be initialized
as an empty list. This attribute will store a list of the book titles that the patron currently has checked out.

The checkOutBook method should have the parameters self, checkOutLimit and bookTitle. If the patron is at their
checkout limit, print a "Sorry" message to the patron. Otherwise, append the bookTitle to the patron's booksCheckedOut
list and print a "Checkout" message, as shown below.

The returnBook method should have the parameters self and book. Here, book is a book list object - you will need to
extract the book title from the list. Remove the book title from the patron's list of checked out book titles and
print a "returned" message.

The printCheckedOutBooks method should have the parameter self. Print a message along and print all the patron's
checked out book titles, as shown below.
"""


class LibraryPatron:
    def __init__(self, name: str):
        self.name = name
        self.booksCheckedOut = []

    def checkOutBook(self, checkOutLimit: int, bookTitle: str):
        if len(self.booksCheckedOut) >= checkOutLimit:
            print(f"Sorry {self.name} you are at your limit of {checkOutLimit} books")
        else:
            self.booksCheckedOut.append(bookTitle)
            print(f"{self.name} has checked out {bookTitle}")

    def returnBook(self, book: []):
        bookTitle = book[0]
        if bookTitle in self.booksCheckedOut:
            self.booksCheckedOut.remove(bookTitle)
            print(f"{self.name} has returned {bookTitle}")

    def printCheckedOutBooks(self):
        if len(self.booksCheckedOut) > 0:
            print(f"{self.name} has the following books checked out:")
            print("\n".join(self.booksCheckedOut))
        else:
            print(f"{self.name} has the no books checked out")


"""
AdultPatron class:

The AdultPatron class inherits from the LibraryPatron class and has the following two methods: __init__, checkOutBook.

The __init__ method should have the parameters self and name. Call LibraryPatron's __init__ to store the name.
There should also be an additional attribute called checkOutLimit which should be initialized with a value of 4.

The checkOutBook method should have the parameters self and book. Here again, book is a book list object.
Call LibraryPatron's checkOutBook method, using the patron's checkOutLimit and the book title as arguments.
"""


class AdultPatron(LibraryPatron):
    checkOutLimit = 4

    def __init__(self, name: str):
        super(AdultPatron, self).__init__(name)

    def checkOutBook(self, book: []):
        bookTitle = book[0]
        super(AdultPatron, self).checkOutBook(AdultPatron.checkOutLimit, bookTitle)


"""
JuvenilePatron class:

The JuvenilePatron class inherits from the LibraryPatron class and has the following two methods: __init__,
checkOutBook.

The __init__ method should have the parameters self and name. Call LibraryPatron's __init__ to store the name.
There should also be an additional attribute called checkOutLimit which should be initialized with a value of 2.

The checkOutBook method should have the parameters self and book. Here again, book is a book list object.
If the book is not a a juvenile book, print a "Sorry" message as shown below. Otherwise, call LibraryPatron's
checkOutBook method, using the patron's checkOutLimit and the book title as arguments.
"""


class JuvenilePatron(LibraryPatron):
    checkOutLimit = 2

    def __init__(self, name: str):
        super(JuvenilePatron, self).__init__(name)

    def checkOutBook(self, book: []):
        bookTitle = book[0]
        bookCategory = book[-1]
        if bookCategory == "Juvenile":
            super(JuvenilePatron, self).checkOutBook(
                JuvenilePatron.checkOutLimit, bookTitle
            )
        else:
            print(f"Sorry {self.name} {bookTitle} is an adult book")


if __name__ == "__main__":
    book1 = ["Alice in Wonderland", "Juvenile"]
    book2 = ["The Cat in the Hat", "Juvenile"]
    book3 = ["Harry Potter and the Sorcerer's Stone", "Juvenile"]
    book4 = ["The Hobbit", "Juvenile"]
    book5 = ["The Da Vinci Code", "Adult"]
    book6 = ["The Girl with the Dragon Tattoo", "Adult"]

    patron1 = JuvenilePatron("Jimmy")
    patron2 = AdultPatron("Sophia")

    patron1.checkOutBook(book6)
    patron1.checkOutBook(book1)
    patron1.checkOutBook(book2)
    patron1.printCheckedOutBooks()
    patron1.checkOutBook(book3)
    patron1.returnBook(book1)
    patron1.checkOutBook(book3)
    patron1.printCheckedOutBooks()
    patron2.checkOutBook(book5)
    patron2.checkOutBook(book4)
    patron2.printCheckedOutBooks()


"""
Execution results:

Sorry Jimmy The Girl with the Dragon Tattoo is an adult book
Jimmy has checked out Alice in Wonderland
Jimmy has checked out The Cat in the Hat
Jimmy has the following books checked out:
Alice in Wonderland
The Cat in the Hat
Sorry Jimmy you are at your limit of 2 books
Jimmy has returned Alice in Wonderland
Jimmy has checked out Harry Potter and the Sorcerer's Stone
Jimmy has the following books checked out:
The Cat in the Hat
Harry Potter and the Sorcerer's Stone
Sophia has checked out The Da Vinci Code
Sophia has checked out The Hobbit
Sophia has the following books checked out:
The Da Vinci Code
The Hobbit
"""
