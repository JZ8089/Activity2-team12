"""
Filename: library.py
Description: Library class used for SWEN-352 mocking activity.
"""

from library.patron import Patron
from library.library_db_interface import Library_DB
from library.ext_api_interface import Books_API

class Library:
    """Class used to represent a library."""

    def __init__(self):
        """Constructor for the Library class."""
        self.db = Library_DB()
        self.api = Books_API()

    ############################################################################
    ################################ API METHODS ###############################
    ############################################################################

    def is_ebook(self, book):
        """Checks if the book is an e-book.
        
        :param book: the title of the book
        :returns: True if yes, False if not
        """
        ebooks = self.api.get_ebooks(book)
        book = book.lower()
        for ebook in ebooks:
            if book == ebook['title'].lower():
                return True
        return False

    def get_ebooks_count(self, book):
        """Gets the number of ebooks for a given book.
        
        :param book: the title of the book
        :returns: the number of ebooks
        """
        ebooks = self.api.get_ebooks(book)
        ebook_count = 0
        for ebook in ebooks:
            ebook_count += ebook['ebook_count']
        return ebook_count

    def is_book_by_author(self, author, book):
        """Determines if the book was written by a given author.
        
        :param author: the name of the author
        :param book: the name of the book
        :returns: True if the book was written by the author, False if not
        """
        results = self.api.books_by_author(author)
        for result in results:
            if book.lower() == result.lower():
                return True
        return False

    def get_languages_for_book(self, book):
        """Get the available languages for a given book.
        
        :param book: the title of the book
        :returns: the set of languages the book is available in
        """
        books_info = self.api.get_book_info(book)
        lang_set = set()
        for book in books_info:
            if 'language' in book:
                lang_set.update(book['language'])
        return lang_set

    ############################################################################
    ################################# DB METHODS ###############################
    ############################################################################

    def register_patron(self, fname, lname, age, memberID):
        """Registers a Patron with the library and adds them to the database.
        
        :param fname: the Patron's first name
        :param lname: the Patron's last name
        :param age: the Patron's age
        :param memberID: the ID of the Patron
        :returns: None if the Patron is already in the database, else their ID
        """
        patron = Patron(fname, lname, age, memberID)
        return self.db.insert_patron(patron)

    def is_patron_registered(self, patron):
        """Determines if the Patron is already registered in the database.
        
        :param patron: the Patron object
        :returns: True if they are in the database, False if not
        """
        reg_patron = self.db.retrieve_patron(patron.get_memberID())
        if reg_patron:
            return True
        return False

    def borrow_book(self, book, patron):
        """Borrows a book for a Patron.
        
        :param book: the title of the book
        :param patron: the Patron object
        """
        patron.add_borrowed_book(book.lower())
        self.db.update_patron(patron)

    def return_borrowed_book(self, book, patron):
        """Returns a borrowed book for a Patron.
        
        :param book: the title of the book
        :param patron: the Patron object
        """
        patron.return_borrowed_book(book.lower())
        self.db.update_patron(patron)

    def is_book_borrowed(self, book, patron):
        """Determines if the Patron has borrowed a given book.
        
        :param book: the title of the book
        :param patron: the Patron object
        :returns: True if the Patron has borrowed the book, False if not
        """
        borrowed_books = patron.get_borrowed_books()
        return book.lower() in borrowed_books
