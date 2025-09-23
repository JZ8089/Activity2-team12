"""
Filename: ext_api_interface.py
Description: module used for interacting with a web service
"""

import requests

class Books_API:
    """Class used for interacting with the OpenLibrary API."""

    API_URL = "http://openlibrary.org/search.json"

    def make_request(self, url):
        """Makes a HTTP request to the given URL.
        
        :param url: the url used for the HTTP request
        :returns: the JSON body of the request, None if non 200 status code or ConnectionError
        """
        try:
            response = requests.get(url)
            if response.status_code != 200:
                return None
            return response.json()
        except requests.ConnectionError:
            return None

    def is_book_available(self, book):
        """Determines if a given book is available to borrow.
        
        :param book: the title of the book
        :returns: True if available, False if not
        """
        request_url = "%s?q=%s" % (self.API_URL, book)
        json_data = self.make_request(request_url)
        if json_data and len(json_data['docs']) >= 1:
            return True
        return False

    def books_by_author(self, author):
        """Gets all the books written by a given author.
        
        :param author: the name of the author
        :returns: the titles of all the books in a list form
        """
        request_url = "%s?author=%s" % (self.API_URL, author)
        json_data = self.make_request(request_url)
        if not json_data:
            return []
        books = []
        for book in json_data['docs']:
            books.append(book['title_suggest'])
        return books

    def get_book_info(self, book):
        """Gets the information for a given book.
        
        :param book: the title of the book
        :returns: a list of dictionaries with book data
        """
        request_url = "%s?q=%s" % (self.API_URL, book)
        json_data = self.make_request(request_url)
        if not json_data:
            return []
        books_info = []
        for book in json_data['docs']:
            info = {'title': book['title']}
            if 'publisher' in book:
                info.update({'publisher': book['publisher']})
            if 'publish_year' in book:
                info.update({'publish_year': book['publish_year']})
            if 'language' in book:
                info.update({'language': book['language']})
            books_info.append(info)
        return books_info

    def get_ebooks(self, book):
        """Gets the ebooks for a given book.
        
        :param book: the title of the book
        :returns: data about the ebooks
        """
        request_url = "%s?q=%s" % (self.API_URL, book)
        json_data = self.make_request(request_url)
        if not json_data:
            return []
        ebooks = []
        for book in json_data['docs']:
            if book['ebook_count_i'] >= 1:
                ebooks.append({'title': book['title'], 'ebook_count': book['ebook_count_i']})
        return ebooks
