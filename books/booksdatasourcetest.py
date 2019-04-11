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
        self.books_checker = booksdatasource.BooksDataSource("books.csv", "authors.csv", "books_authors.csv")

    def tearDown(self):
        pass


    #  Book function tests


    def test_zero_book(self):
        self.assertEqual(self.books_checker.book(0), "All Clear")

    def test_negative_book(self):
        self.assertRaises(ValueError,self.books_checker.book, -1)

    def test_larger_than_max_book(self):
        self.assertRaises(ValueError,self.books_checker.book, 100)


    # Books function tests


    def test_invalid_id_books(self):
        self.assertRaises(ValueError, self.books_checker.books, author_id=-1)

    def test_valid_id_books(self):
        self.assertEqual(self.books_checker.books(author_id=0), ['All Clear'])

    def test_search_text_books(self):
        self.assertEqual(self.books_checker.books(search_text="Jane"), ["Jane Eyre"])

    def test_start_year__default_books(self):
        self.assertEqual(self.books_checker.books(start_year=2010), ["All Clear", "Blackout"])

    def test_end_year_books(self):
        self.assertEqual(self.books_checker.books(end_year=1760), ["The Life and Opinions of Tristram Shandy, Gentleman"])

    def test_search_by_title_books(self):
        self.assertEqual(self.books_checker.books(start_year=2010, sort_by="title"), ["All Clear", "Blackout"])

    def test_search_by_year_same_year_books(self):
        self.assertEqual(self.books_checker.books(start_year=2010, sort_by="year"), ["All Clear", "Blackout"])

    def test_no_parameters_returns_list_books(self):
        booksList = self.books_checker.books()
        self.assertTrue(booksList, list)

    def test_no_parameters_returns_dictionaries_books(self):
        booksList = self.books_checker.books()
        self.assertTrue(booksList[0], dictionary)
        # Because books is an empty function, there is no list returned
        # so booksList is an empty list and there's an error here

    def test_start_year_too_big_books(self):
        self.assertEqual(self.books_checker.books(start_year=3000), [])

    def test_end_year_too_small_books(self):
        self.assertEqual(self.books_checker.books(end_year=0), [])

    def end_year_before_start_year_books(self):
        self.assertEqual(self.books_checker.books(start_year=1800, end_year=1700), [])


    # Authors function tests


    def test_invalid_id_authors(self):
        self.assertRaises(ValueError, self.books_checker.authors, book_id=-1)

    def test_valid_id_authors(self):
        self.assertEqual(self.books_checker.authors(book_id=0),["Connie", "Willis"])

    def test_search_text_authors(self):
        self.assertEqual(self.books_checker.authors(search_text="Ton"), [["Toni", "Morrison"],["Toni", "Morrison"]])

    def test_start_year_authors(self):
        self.assertEqual(self.books_checker.authors(start_year=1976), [["Naomi", "Alderman"]])

    def test_end_year_authors(self):
        self.assertEqual(self.books_checker.authors(end_year=1776), [["Jane", "Austen"]])

    def test_search_by_birth_year_authors(self):
        self.assertEqual(self.books_checker.authors(start_year=1945, end_year=1947, sort_by="birth_year"), [["Salman", "Rushdie"], ["Connie", "Willis"]])

    def test_search_by_default_authors(self):
        self.assertEqual(self.books_checker.authors(start_year=1945, end_year=1947), [["Salman", "Rushdie"], ["Connie", "Willis"]])

    def test_no_parameters_returns_list_authors(self):
        authorsList = self.books_checker.authors()
        self.assertTrue(authorsList, list)

    def test_no_parameters_returns_dictionaries_authors(self):
        authorsList = self.books_checker.authors()
        self.assertTrue(authorsList[0], dictionary)
        # Because authors is an empty function, there is no list returned
        # so authorsList is an empty list and there's an error here

    def test_start_year_too_big_authors(self):
        self.assertEqual(self.books_checker.authors(start_year=3000), [])

    def test_end_year_too_small_authors(self):
        self.assertEqual(self.books_checker.authors(end_year=0), [])

    def end_year_before_start_year_authors(self):
        self.assertEqual(self.books_checker.authors(start_year=1800, end_year=1700), [])


    # Author function tests


    def test_zero_authors(self):
        self.assertEqual(self.books_checker.author(0), "Willis, Connie")

    def test_negative_authors(self):
        self.assertRaises(ValueError,self.books_checker.author, -1)

    def test_larger_than_max_author(self):
        self.assertRaises(ValueError,self.books_checker.author, 100)

if __name__ == '__main__':
    unittest.main()
