import unittest
from library import ext_api_interface
from unittest.mock import Mock
import requests
import json

class TestExtApiInterface(unittest.TestCase):
    def setUp(self):
        self.api = ext_api_interface.Books_API()
        self.book = "learning python"
        with open('tests_data/ebooks.txt', 'r') as f:
            self.books_data = json.loads(f.read())
        with open('tests_data/json_data.txt', 'r') as f:
            self.json_data = json.loads(f.read())

    def test_make_request_True(self):
        attr = {'json.return_value': dict()}
        requests.get = Mock(return_value = Mock(status_code = 200, **attr))
        self.assertEqual(self.api.make_request(""), dict())

    def test_make_request_connection_error(self):
        ext_api_interface.requests.get = Mock(side_effect=requests.ConnectionError)
        url = "some url"
        self.assertEqual(self.api.make_request(url), None)

    def test_make_request_False(self):
        requests.get = Mock(return_value=Mock(status_code=100))
        self.assertEqual(self.api.make_request(""), None)

    def test_get_ebooks(self):
        self.api.make_request = Mock(return_value=self.json_data)
        self.assertEqual(self.api.get_ebooks(self.book), self.books_data)

    def test_get_ebooks_false(self):
        self.api.make_request = Mock(return_value=None)
        self.assertEqual(self.api.get_ebooks("doesnt exist"), [])
        
    def test_is_book_available_true(self):
        self.api.make_request = Mock(return_value=self.json_data)
        self.assertEqual(self.api.is_book_available(self.book),True)
        
    def test_is_book_available_false(self):
        self.api.make_request = Mock(return_value=None)
        self.assertEqual(self.api.is_book_available("doesnt exist"),False)

    def test_books_by_author_false(self):
        self.api.make_request = Mock(return_value=None)
        self.assertEqual(self.api.books_by_author("doesnt exist"),[])

    def test_books_by_author_true(self):
        self.api.make_request = Mock(return_value=self.json_data)
        expected_ouput = ['Learning Python', 'Learning Python (Learning)', 'Learning Python', 'Learning Python', 'Python Machine Learning', 'Python machine learning', 'Learn Python Visually', 'Learn Python Quickly', 'Python Machine Learning', 'Python Machine Learning', 'Learn Python-3', 'Learning With Python', 'Machine Learning in Python', 'Deep Learning with Python', 'Learning Robotics Using Python', 'Learn Python for Beginners', 'Machine Learning with Python', 'Learning Python Data Visualization', 'Learning Python Application Development', 'Deep Learning with Python', 'Python Machine Learning Cookbook', 'Learning Python for Forensics', '  Deep learning con Python ', 'Learning Python with Raspberry Pi', 'Learn to Program Using Python', 'Learning Scientific Programming with Python', 'Applied Reinforcement Learning with Python', 'Learn Python the Hard Way', 'Learning Python With Raspberry Pi', 'Free eBook - Learning Python', 'Learning Python by Building Games', 'PYTHON MACHINE LEARNING CASE STUDIES', 'Machine Learning Applications Using Python', 'Learn to Program with Python', 'Learn Python Programming for Beginners', 'Learn to Program with Python', 'Learn Python in 24 Hours', 'Learning BeagleBone Python Programming', 'Thoughtful Machine Learning with Python', 'Advanced Machine Learning with Python', 'Python: Real World Machine Learning', 'Learn to program using Python', 'Learn Python in one hour', 'Learning to Program in Python', 'Python Machine Learning: Machine Learning and Deep Learning with Python, scikit-learn, and TensorFlow, 2nd Edition', 'Lean Python: Learn Just Enough Python to Build Useful Tools', 'Python for Beginners: 2018 Edition: Learn to Code with Python!', 'Learn Python in 7 Days: Begin your journey with Python', 'Machine Learning with Spark and Python', 'Hands on Machine Learning with Python', 'Machine Learning with Python for Everyone', 'Deep Learning mit Python und Keras', 'Large Scale Machine Learning with Python', 'Building Machine Learning Systems with Python', 'Learn Raspberry Pi Programming with Python', 'Python: Deeper Insights into Machine Learning', 'Introduction to Machine Learning with Python', 'Learn Python in One Day and Learn It Well', 'Python', 'Python', 'Python', 'Python', 'Python', 'Python for Probability, Statistics, and Machine Learning', 'Learn Quantum Computing with Python and Q#', 'Get Programming: Learn to code with Python', 'Python Deep Learning Cookbook: Over 75 practical recipes on neural network modeling, reinforcement learning, and transfer learning using Python', 'Learning Python Web Penetration Testing: Automate web penetration testing activities using Python', 'Machine Learning and Deep Learning Using Python and TensorFlow', 'Practical Machine Learning for Data Analysis Using Python', 'Python Workbook', 'Hands-On Machine Learning with Scikit-learn and Scientific Python Toolkits', 'Hands-On Machine Learning with scikit-learn and Scientific Python Toolkits', 'Python Programming', 'Python Basics', 'Python 3', 'Mastering Machine Learning with Python in Six Steps', 'Machine Learning for Time Series Forecasting with Python', 'Python Programming, Deep Learning : 3 Books in 1', 'Learning to Program Using Python 2nd Ed.', 'Beginning Anomaly Detection Using Python-Based Deep Learning', 'Building Machine Learning Systems with Python - Second Edition', 'Hands-On Data Science and Python Machine Learning', 'Learn Data Analysis with Python: Lessons in Coding', 'Deep Learning with Python: A Hands-on Introduction', 'Python Programming', 'Python Programming', 'Python Programming', 'Python Programming', 'Aprendendo Python', 'Python Basics', 'Machine Learning with Python Cookbook: Practical Solutions from Preprocessing to Deep Learning', 'Learning Python for Forensics: Leverage the power of Python in forensic investigations, 2nd Edition', 'Learn Web Development with Python: Get hands-on with Python Programming and Django web development', 'Python: Advanced Guide to Artificial Intelligence: Expert machine learning systems and intelligent agents using Python', 'Learning OpenCV 4 Computer Vision with Python 3', 'Machine Learning in Python: Essential Techniques for Predictive Analysis', 'Python for Beginners', 'Python Data Analytics', 'Advanced Data Analytics Using Python: With Machine Learning, Deep Learning and NLP Examples']
        self.assertEqual(self.api.books_by_author(self.book),expected_ouput)

    def test_get_book_info_false(self):
        self.api.make_request = Mock(return_value=None)
        self.assertEqual(self.api.get_book_info("doesnt exist"),[])

    # def test_get_book_info_true(self):
    #     self.api.make_request = Mock(return_value=None)
    #     print()
    #     self.assertEqual(self.api.get_book_info("doesnt exist"),False)
