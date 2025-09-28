import unittest
from unittest.mock import MagicMock, patch
from library.library_db_interface import Library_DB
from library.patron import Patron


class TestLibraryDB(unittest.TestCase):
    def setUp(self):
        # Patch TinyDB so no real file db.json is created
        patcher = patch("library.library_db_interface.TinyDB")
        self.addCleanup(patcher.stop)
        self.mock_tinydb = patcher.start()
        self.mock_db = MagicMock()
        self.mock_tinydb.return_value = self.mock_db

        self.db = Library_DB()
        self.patron = Patron("John", "Doe", 25, "123")

    # ------------------------
    # insert_patron
    # ------------------------
    def test_insert_patron_none(self):
        self.assertIsNone(self.db.insert_patron(None))

    def test_insert_patron_already_exists(self):
        self.db.retrieve_patron = MagicMock(return_value=self.patron)
        self.assertIsNone(self.db.insert_patron(self.patron))

    def test_insert_patron_success(self):
        self.db.retrieve_patron = MagicMock(return_value=None)
        self.db.convert_patron_to_db_format = MagicMock(return_value={"mock": "data"})
        self.mock_db.insert.return_value = 42
        result = self.db.insert_patron(self.patron)
        self.assertEqual(result, 42)
        self.mock_db.insert.assert_called_once_with({"mock": "data"})

    # ------------------------
    # get_patron_count
    # ------------------------
    def test_get_patron_count(self):
        self.mock_db.all.return_value = [1, 2, 3]
        self.assertEqual(self.db.get_patron_count(), 3)

    # ------------------------
    # get_all_patrons
    # ------------------------
    def test_get_all_patrons(self):
        self.mock_db.all.return_value = ["a", "b"]
        self.assertEqual(self.db.get_all_patrons(), ["a", "b"])

    # ------------------------
    # update_patron
    # ------------------------
    def test_update_patron_none(self):
        self.assertIsNone(self.db.update_patron(None))

    def test_update_patron_success(self):
        self.db.convert_patron_to_db_format = MagicMock(return_value={"mock": "data"})
        self.db.update_patron(self.patron)
        self.mock_db.update.assert_called_once()

    # ------------------------
    # retrieve_patron
    # ------------------------
    def test_retrieve_patron_found(self):
        self.mock_db.search.return_value = [{
            "fname": "Jane", "lname": "Smith", "age": 30, "memberID": "abc"
        }]
        result = self.db.retrieve_patron("abc")
        self.assertIsInstance(result, Patron)
        self.assertEqual(result.get_fname(), "Jane")

    def test_retrieve_patron_not_found(self):
        self.mock_db.search.return_value = []
        self.assertIsNone(self.db.retrieve_patron("missing"))

    # ------------------------
    # close_db
    # ------------------------
    def test_close_db(self):
        self.db.close_db()
        self.mock_db.close.assert_called_once()

    # ------------------------
    # convert_patron_to_db_format
    # ------------------------
    def test_convert_patron_to_db_format(self):
        result = self.db.convert_patron_to_db_format(self.patron)
        self.assertEqual(result["fname"], "John")
        self.assertEqual(result["lname"], "Doe")
        self.assertEqual(result["age"], 25)
        self.assertEqual(result["memberID"], "123")
        self.assertEqual(result["borrowed_books"], self.patron.get_borrowed_books())
        


if __name__ == "__main__":
    unittest.main()
