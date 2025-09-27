import unittest
from library import patron

class TestPatron(unittest.TestCase):

    def setUp(self):
        self.pat = patron.Patron('fname', 'lname', '20', '1234')
        self.book = "learning python"

    def test_valid_name(self):
        pat = patron.Patron('fname', 'lname', '20', '1234')
        self.assertTrue(isinstance(pat, patron.Patron))

    def test_invalid_name(self):
        self.assertRaises(patron.InvalidNameException, patron.Patron, '1fname', '1lname', '20', '1234')

    def test_add_borrowed_book_and_get_borrowed_books(self):
        self.pat.add_borrowed_book(self.book)
        self.pat.add_borrowed_book("second book")
        self.assertEqual(self.pat.get_borrowed_books(), [self.book, "second book"])
        
    def test_add_borrowed_book_twice(self):
        self.pat.add_borrowed_book(self.book)
        self.pat.add_borrowed_book(self.book)
        self.assertEqual(self.pat.get_borrowed_books(), [self.book])
        
    def test_return_borrowed_book(self):
        self.pat.add_borrowed_book(self.book)
        self.pat.add_borrowed_book("second book")
        self.pat.return_borrowed_book(self.book)
        self.assertEqual(self.pat.get_borrowed_books(), ["second book"])
    
    def test_eq(self):
        pat2 = patron.Patron('fname', 'lname', '20', '1234')
        self.assertEqual(self.pat,pat2)
    
    def test_ne(self):
        pat3 = patron.Patron('different', 'different', '20', '1234')
        self.assertNotEqual(self.pat,pat3)
        
    def test_get_fname(self):
        self.assertEqual(self.pat.get_fname(),"fname")
        
    def test_get_lname(self):
        self.assertEqual(self.pat.get_lname(),"lname")
        
    def test_get_age(self):
        self.assertEqual(self.pat.get_age(),"20")
        
    def test_get_memberID(self):
        self.assertEqual(self.pat.get_memberID(),"1234")
    