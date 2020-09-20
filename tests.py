import unittest
import test_inputs

KEY = 'NO3OQeyssAHJokwZ0iOPeQ'
TEST_DATA = test_inputs.json_data


class TestGoodReadsScriptMethods(unittest.TestCase):
    def test_make_url(self):
        url = TEST_DATA.get('url_input')
        formatted_url = url + '.xml?key={}'.format(KEY)
        self.assertEqual(formatted_url, TEST_DATA.get('url_output'))

    def test_get_authors(self):
        authors = TEST_DATA.get('authors')
        multiple_authors = TEST_DATA.get('multiple_authors')
        if not authors or multiple_authors:
            return None
        author = authors.get('author')
        multiple_author = multiple_authors.get('author')
        if isinstance(multiple_author, list):
            names = ', '.join([name.get('name') for name in author])
            self.assertEqual(names, TEST_DATA.get('list_names'))
        names = author.get('name')
        self.assertEqual(names, TEST_DATA.get('name'))


if __name__ == '__main__':
    unittest.main()
