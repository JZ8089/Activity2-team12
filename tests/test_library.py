import unittest
from unittest.mock import Mock
from library import library
import json

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.lib = library.Library()
        self.books_data = [{'title': 'Learning Python', 'ebook_count': 3}, {'title': 'Learning Python (Learning)', 'ebook_count': 1}, {'title': 'Learning Python', 'ebook_count': 1}, {'title': 'Learn to Program Using Python', 'ebook_count': 1}, {'title': 'Aprendendo Python', 'ebook_count': 1}, {'title': 'Python Basics', 'ebook_count': 1}]
        with open('tests_data/ebooks.txt', 'r') as f:
            self.books_data = json.loads(f.read())


    #is ebook
    def test_is_ebook_true(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertTrue(self.lib.is_ebook('learning python'))

    def test_is_ebook_false(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertFalse(self.lib.is_ebook('learning pythagorean'))

    #get ebooks count
    def test_get_ebooks_count(self):
        self.lib.api.get_ebooks = Mock(return_value=self.books_data)
        self.assertEqual(self.lib.get_ebooks_count("learning python"), 8)

    #is book by author
    def test_is_book_by_author_true(self):
        self.lib.api.books_by_author = Mock(return_value=["Learning Python", "Python Cookbook"])
        self.assertTrue(self.lib.is_book_by_author("John Python idk", "Learning Python"))

    def test_is_book_by_author_false(self):
        self.lib.api.books_by_author = Mock(return_value=["Learn to Program Using Python", "Eating python code"])
        self.assertFalse(self.lib.is_book_by_author("Steve Python", "Learning Python"))

    #getting languages
    def test_get_languages_for_book_true(self):
        self.lib.api.get_book_info = Mock(return_value=[{"title": "Learning Python", "language": ["english"]}])
        self.assertEqual(self.lib.get_languages_for_book("Learning Python"), {"english"})

    def test_get_languages_for_book_false(self):
        self.lib.api.get_book_info = Mock(return_value=[{"title": "Learning Python", "language": ["english"]}])
        self.assertNotIn("french", self.lib.get_languages_for_book("Learning Python"))

    #register patron
    def test_register_patron(self):
        self.lib.db.insert_patron = Mock(return_value="00001")
        result = self.lib.register_patron("John", "Python", 82, "00001")
        self.assertEqual(result, "00001")

    #is patron registered
    def test_is_patron_registered_true(self):
        patron = Mock()
        patron.get_memberID = Mock(return_value="00002")
        self.lib.db.retrieve_patron = Mock(return_value=patron)
        result = self.lib.is_patron_registered(patron)
        self.assertTrue(result)

    #borrow book
    def test_borrow_book(self):
        patron = Mock()
        self.lib.db.update_patron = Mock()
        self.lib.borrow_book("Learning Python", patron)
        patron.add_borrowed_book.assert_called_once_with("learning python")

    #return book
    def test_return_borrowed_book(self):
        patron = Mock()
        self.lib.db.update_patron = Mock()
        self.lib.borrow_book("Learning Python", patron)
        self.lib.return_borrowed_book("Learning Python", patron)
        patron.return_borrowed_book.assert_called_once_with("learning python")

    #is book borrowed
    def test_is_book_borrowed_true(self):
        patron = Mock()
        patron.get_borrowed_books = Mock(return_value=["learning python"])
        result = self.lib.is_book_borrowed("Learning Python", patron)
        self.assertTrue(result)
    
    def test_is_book_borrowed_true(self):
        patron = Mock()
        patron.get_borrowed_books = Mock(return_value=["learning python"])
        result = self.lib.is_book_borrowed("Learning C#", patron)
        self.assertFalse(result)