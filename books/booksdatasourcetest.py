'''
booksdatasourcetest.py
4/12/19
Kate Grossman and Ginnie White

A program that contains unit tests for booksdatasource.py. Tests are broken up
in the code based on what method they're testing.

'''
import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):

    def setUp(self):
        self.books_checker = booksdatasource.BooksDataSource("books.csv", "authors.csv",
        "books_authors.csv")

    def tearDown(self):
        pass


    #  Book function tests

    def test_zero_book(self):
        self.assertEqual(self.books_checker.book(0), {'id': '0', 'title': 'All Clear', 'publication_year': '2010'})

    def test_negative_book(self):
        self.assertRaises(ValueError,self.books_checker.book, "-1")

    def test_larger_than_max_book(self):
        self.assertRaises(ValueError,self.books_checker.book, "100")



    # Books function tests

    def test_invalid_id_books(self):
        self.assertRaises(ValueError, self.books_checker.books, author_id="-1")

    def test_valid_id_books(self):
        self.assertEqual(self.books_checker.books(author_id="0"), [{'id': '0', 'title': 'All Clear', 'publication_year': '2010'},
        {'id': '3', 'title': 'Blackout', 'publication_year': '2010'},
        {'id': '27', 'title': 'To Say Nothing of the Dog', 'publication_year': '1997'}])

    def test_search_text_books(self):
        self.assertEqual(self.books_checker.books(search_text="Jane"),
        [{'id': '7', 'title': 'Jane Eyre', 'publication_year': '1847'}])

    def test_start_year__default_books(self):
        self.assertEqual(self.books_checker.books(start_year="2016"),
        [{'id': '35', 'title': 'The Power', 'publication_year': '2016'}])

    def test_end_year_books(self):
        self.assertEqual(self.books_checker.books(end_year="1813"),
        [{'id': '18', 'title': 'Pride and Prejudice', 'publication_year': '1813'},
        {'id': '20', 'title': 'Sense and Sensibility', 'publication_year': '1813'}])

    def test_search_by_title_books(self):
        self.assertEqual(self.books_checker.books(start_year="2015", sort_by="title"),
        [{'id': '37', 'title': 'The Fifth Season', 'publication_year': '2015'},
        {'id': '38', 'title': 'The Obelisk Gate', 'publication_year': '2015'},
        {'id': '35', 'title': 'The Power', 'publication_year': '2016'},
        {'id': '39', 'title': 'The Stone Sky', 'publication_year': '2015'}])

    def test_search_by_year_books(self):
        self.assertEqual(self.books_checker.books(start_year="2015", sort_by="year"),
        [{'id': '37', 'title': 'The Fifth Season', 'publication_year': '2015'},
        {'id': '38', 'title': 'The Obelisk Gate', 'publication_year': '2015'},
        {'id': '39', 'title': 'The Stone Sky', 'publication_year': '2015'},
        {'id': '35', 'title': 'The Power', 'publication_year': '2016'}])

    def test_no_parameters_returns_list_books(self):
        booksList = self.books_checker.books()
        self.assertTrue(booksList, list)

    def test_no_parameters_returns_dictionaries_books(self):
        booksList = self.books_checker.books()
        self.assertTrue(booksList[0], dict)

    def test_start_year_too_big_books(self):
        self.assertEqual(self.books_checker.books(start_year="3000"), [])

    def test_end_year_too_small_books(self):
        self.assertEqual(self.books_checker.books(end_year="0"), [])

    def end_year_before_start_year_books(self):
        self.assertEqual(self.books_checker.books(start_year="1800", end_year="1700"), [])


    # Authors function tests

    def test_invalid_id_authors(self):
        self.assertRaises(ValueError, self.books_checker.authors, book_id="-1")

    def test_valid_id_authors(self):
        self.assertEqual(self.books_checker.authors(book_id="0"),
        [{'id': '0', 'last_name': 'Willis', 'first_name': 'Connie', 'birth_year': '1945', 'death_year': 'NULL'}])

    def test_search_text_authors(self):
        self.assertEqual(self.books_checker.authors(search_text="Toni"),
        [{'id': '2', 'last_name': 'Morrison', 'first_name': 'Toni', 'birth_year': '1931', 'death_year': 'NULL'}])

    def test_start_year_is_latest_year_authors(self):
        self.assertEqual(self.books_checker.authors(start_year="2016"),
        [{'id': '18', 'last_name': 'Alderman', 'first_name': 'Naomi',
         'birth_year': '1974', 'death_year': 'NULL'}, {'id': '12',
         'last_name': 'Bujold', 'first_name': 'Lois McMaster', 'birth_year': '1949',
         'death_year': 'NULL'}, {'id': '24', 'last_name': 'Carré', 'first_name': 'John Le',
          'birth_year': '1931', 'death_year': 'NULL'}, {'id': '5', 'last_name': 'Gaiman',
           'first_name': 'Neil', 'birth_year': '1960', 'death_year': 'NULL'},
           {'id': '20', 'last_name': 'Jemisen', 'first_name': 'N.K.',
           'birth_year': '1972', 'death_year': 'NULL'}, {'id': '3', 'last_name': 'Lewis',
            'first_name': 'Sinclair', 'birth_year': '1885', 'death_year': 'NULL'},
            {'id': '2', 'last_name': 'Morrison', 'first_name': 'Toni',
            'birth_year': '1931', 'death_year': 'NULL'}, {'id': '16', 'last_name': 'Murakami',
            'first_name': 'Haruki', 'birth_year': '1949', 'death_year': 'NULL'},
            {'id': '11', 'last_name': 'Rushdie', 'first_name': 'Salman',
             'birth_year': '1947', 'death_year': 'NULL'},
              {'id': '0', 'last_name': 'Willis', 'first_name': 'Connie',
               'birth_year': '1945', 'death_year': 'NULL'}])

    def test_end_year_is_earliest_year_authors(self):
        self.assertEqual(self.books_checker.authors(end_year="1776"),
        [{'id': '4', 'last_name': 'Austen', 'first_name': 'Jane',
        'birth_year': '1775', 'death_year': '1817'}])

    #def test_search_by_birth_year_authors(self):
        #self.assertEqual(self.books_checker.authors(start_year="1945", end_year="1947",
        #sort_by="birth_year"), [["Salman", "Rushdie"], ["Connie", "Willis"]])

    #def test_search_by_default_authors(self):
        #self.assertEqual(self.books_checker.authors(start_year="1945", end_year="1947"),
        #[["Salman", "Rushdie"], ["Connie", "Willis"]])

    def test_no_parameters_returns_list_authors(self):
        authorsList = self.books_checker.authors()
        self.assertTrue(authorsList, list)

    def test_no_parameters_returns_dictionaries_authors(self):
        authorsList = self.books_checker.authors()
        self.assertTrue(authorsList[0], dict)
        # Because authors is an empty function, there is no list returned
        # so authorsList is an empty list and there's an error here

    def test_start_year_too_big_authors(self):
        self.assertEqual(self.books_checker.authors(start_year="3000"), [])

    def test_end_year_too_small_authors(self):
        self.assertEqual(self.books_checker.authors(end_year="0"), [])

    def end_year_before_start_year_authors(self):
        self.assertEqual(self.books_checker.authors(start_year="1800", end_year="1700"), [])


    # Author function tests

    def test_zero_author(self):
        self.assertEqual(self.books_checker.author(0), {"id":"0", "last_name":"Willis",
        "first_name": "Connie", "birth_year":"1945", 'death_year': 'NULL'})

    def test_negative_author(self):
        self.assertRaises(ValueError,self.books_checker.author, "-1")

    def test_larger_than_max_author(self):
        self.assertRaises(ValueError,self.books_checker.author, "100")


if __name__ == '__main__':
    unittest.main()
