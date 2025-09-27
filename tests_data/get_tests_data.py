import sys
sys.path.append('.')

from library import ext_api_interface
import json


class GetData:
    def __init__(self):
        self.api = ext_api_interface.Books_API()

    def get_ebooks(self, book):
        print("get ebooks: " + book)
        ebooks = self.api.get_ebooks(book)
        print(ebooks)
        with open('tests_data/ebooks.txt', 'w') as f:
            f.write(json.dumps(ebooks))

    def get_json(self, book):
        request_url = "%s?q=%s" % (self.api.API_URL, book)
        json_data = self.api.make_request(request_url)
        print(json_data)
        with open('tests_data/json_data.txt', 'w') as f:
            f.write(json.dumps(json_data))

if __name__ == "__main__":
    getdata = GetData()
    getdata.get_ebooks('learning python')
    getdata.get_json('learning python')
