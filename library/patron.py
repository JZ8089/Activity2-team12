"""
Filename: patron.py
Description: Patron class for SWEN-352 mocking activity.
"""

import re

class InvalidNameException(Exception):
    """Custom Exception for an invalid name."""
    pass

class Patron:
    """Patron class used to represent a user for a library."""

    def  __init__(self, fname, lname, age, memberID):
        """Constructor for the Patron class.

        :param fname: the first name for the Patron
        :param lname: the last name for the Patron
        :param age: the age of the Patron
        :param memberID: the ID for the Patron in the library's system
        """

        if re.search('\d', fname) or re.search('\d', lname):
            raise InvalidNameException("Name should not contain numbers")
        self.fname = fname
        self.lname = lname
        self.age = age
        self.memberID = memberID
        self.borrowed_books = []

    def add_borrowed_book(self, book):
        """Adds a book to the list of borrowed books for the Patron
        
        :param book: the title of the book
        """
        book = book.lower()
        if book in self.borrowed_books:
            return
        self.borrowed_books.append(book)

    def get_borrowed_books(self):
        """Gets the list of borrowed books for the Patron.
        
        :returns: the list of borrowed books
        """
        return self.borrowed_books

    def return_borrowed_book(self, book):
        """Removes the borrowed book from the list of books currently checked out.
        
        :param book: the title of the book to remove
        """
        book = book.lower()
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

    def  __eq__(self, other):
        """Equals function for the Patron class."""
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Not-equal function for the Patron class."""
        return not self.__eq__(other)

    def get_fname(self):
        """Getter for the first name of the Patron.
        
        :returns: the first name of the Patron
        """
        return self.fname

    def get_lname(self):
        """Getter for the last name of the Patron.
        
        :returns: the last name of the Patron
        """
        return self.lname

    def get_age(self):
        """Getter for the age of the Patron.
        
        :returns: the age of the Patron
        """
        return self.age

    def get_memberID(self):
        """Getter for the memberID of the Patron.
        
        :returns: the memberID of the Patron
        """
        return self.memberID