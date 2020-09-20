import sys
import requests
import xmltodict
import json

KEY = 'NO3OQeyssAHJokwZ0iOPeQ'


class InvalidGoodReadsURL(Exception):
    pass


class GoodReadsAPIClient:
    @staticmethod
    def make_url(url):
        formatted_url = url + '.xml?key={}'.format(KEY)
        return formatted_url

    @staticmethod
    def get_authors(authors):
        if not authors:
            return None
        author = authors.get('author')
        if isinstance(author, list):
            names = ', '.join([name.get('name') for name in author])
        else:
            names = author.get('name')
        return names

    def get_book_details(self, book_url):
        fetch_url = self.make_url(book_url)
        request = requests.get(fetch_url)
        status_code = request.status_code
        try:
            if status_code == 200:
                my_dict = xmltodict.parse(request.content.decode())
                json_data = json.loads(json.dumps(my_dict))
                book_data = json_data.get('GoodreadsResponse').get('book')
                review_object = {
                                    'title': book_data.get('title'),
                                    'average_rating': book_data.get('average_rating'),
                                    'ratings_count': book_data.get('ratings_count'),
                                    'num_pages': book_data.get('num_pages'),
                                    'image_url': book_data.get('image_url'),
                                    'publication_year': book_data.get('publication_year'),
                                    'authors': self.get_authors(book_data.get('authors'))
                }
                return review_object
            elif status_code == 404:
                raise InvalidGoodReadsURL
            else:
                return {}
        except Exception as e:
            raise e


cli_url = sys.argv[-1]
book_details = GoodReadsAPIClient()
print(book_details.get_book_details(cli_url))

