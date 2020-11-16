"""
Krupa Dhruva
CIS 41A   Fall 2020
Unit J in-class assignment
"""

import LibraryBook


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

    def returnBook(self, book: LibraryBook.Book):
        bookTitle = book.title
        if book.title in self.booksCheckedOut:
            self.booksCheckedOut.remove(bookTitle)
            print(f"{self.name} has returned {bookTitle}")

    def printCheckedOutBooks(self):
        if len(self.booksCheckedOut) > 0:
            print(f"{self.name} has the following books checked out:")
            print("\n".join(self.booksCheckedOut))
        else:
            print(f"{self.name} has the no books checked out")


class AdultPatron(LibraryPatron):
    checkOutLimit = 4

    def __init__(self, name: str):
        super(AdultPatron, self).__init__(name)

    def checkOutBook(self, book: LibraryBook.Book):
        bookTitle = book.title
        super(AdultPatron, self).checkOutBook(AdultPatron.checkOutLimit, bookTitle)


class JuvenilePatron(LibraryPatron):
    checkOutLimit = 2

    def __init__(self, name: str):
        super(JuvenilePatron, self).__init__(name)

    def checkOutBook(self, book: LibraryBook.Book):
        bookTitle = book.title
        bookCategory = book.bookType
        if bookCategory == "Juvenile":
            super(JuvenilePatron, self).checkOutBook(
                JuvenilePatron.checkOutLimit, bookTitle
            )
        else:
            print(f"Sorry {self.name} {bookTitle} is an adult book")
