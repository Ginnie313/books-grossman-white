'''
    booksdatasourcetest.py

'''
import booksdatasource
import unittest

class BooksDataSourceTest(unittest.TestCase):

    def setUp(self):
        self.books_checker = booksdatasource.BooksDataSource(books.csv, authors.csv, books_authors.csv)

    def tearDown(self):
        pass

    # Book function tests

    def test_zero(self):
        self.assertEqual(self.books_checker.book(0), "All Clear")

    def test_negative(self):
        self.assertRaises(ValueError,self.books_checker.book, -1)

    def test_float(self):
        self.assertRaises(TypeError,self.books_checker.book, 1.0)


    # Books function tests

    def test_invalid_id(self):
        self.assertRaises(ValueError, self.books_checker.books, author_id=-1, search_text=None, start_year=None, end_year=None, sort_by='title')

    #Valid id test
    #Values aren't None or integers (are we allowed to throw a type error?)
    #Values are correctly typed
    #Sort value is default
    #Sort by isn't title, default or year
    #No parameters
    #Start year is higher than end year
    #Start year is lower than end year
    # Authors function tests

    def test_invalid_id(self):
        self.assertRaises(ValueError, self.books_checker.books, book_id=-1, search_text=None, start_year=None, end_year=None, sort_by='birth_year')

    # Author function tests

    def test_zero(self):
        self.assertEqual(self.books_checker.author(0), "Willis, Connie")

    def test_negative(self):
        self.assertRaises(ValueError,self.books_checker.author., -1)

    def test_float(self):
        self.assertRaises(TypeError,self.books_checker.book.author, 1.0)
