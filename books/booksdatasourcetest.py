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

    def test_zero_book(self):
        self.assertEqual(self.books_checker.book(0), "All Clear")

    def test_negative_book(self):
        self.assertRaises(ValueError,self.books_checker.book, -1)

    def test_larger_than_max_book(self):
        self.assertRaises(ValueError,self.books_checker.book, 100)


    # Books function tests

    def test_invalid_id_books(self):
        self.assertRaises(ValueError, self.books_checker.books, -1, None, None, None, 'title')

    def test_valid_id_books(self):
        self.assertRaises(ValueError, self.books_checker.books, 0, None, None, None, 'title')

    def test_search_text_books(self):
        #Tests this one parameter works for a valid case
        self.assertEqual(self.books_checker.books(None, "Jane", None, None, None), ["Jane Eyre"])

    def test_start_year_books(self):
        #Tests this one parameter works for a valid case
        self.assertEqual(self.books_checker.books(None, None, 2010, None, None), ["All Clear", "Blackout"])

    def test_end_year_books(self):
        self.assertEqual(self.books_checker.books(None, None, None, 1760, None), ["The Life and Opinions of Tristram Shandy, Gentleman"])

    def test_search_by_title_books(self):
        #Tests this one parameter works for a valid case
        self.assertEqual(self.books_checker.books(None, None, 2010, None, "title"), ["All Clear", "Blackout"])

    def test_search_by_year_same_year_books(self):
        self.assertEqual(self.books_checker.books(None, None, 2010, None, "year"), ["All Clear", "Blackout"])

    def test_search_by_default_books(self): #possibly get rid of this test
        self.assertEqual(self.books_checker.books(None, None, 2010, None, None), ["All Clear", "Blackout"])

    def test_no_parameters_returns_list_books(self):
        booksList = authors(self.books_checker.books())
        self.assertTrue(booksList, list)

    def test_no_parameters_returns_dictionaries_books(self):
        booksList = authors(self.books_checker.books())
        self.assertTrue(booksList.get(0), dictionary)

    def test_start_year_too_big_books(self):
        assertEqual(self.books_checker.books(None, None, 3000, None, None), [])
        # test that if we start at year 3000, returns empty list

    def test_end_year_too_small_books(self):
        assertEqual(self.books_checker.books(None, None, None, 0, None), [])
        # test that if we end at year 0, returns empty list

    def end_year_before_start_year_books(self):
        assertEqual(self.books_checker.books(None, None, 1800, 1700, None), [])

    # Authors function tests

    def test_invalid_id_authors(self):
        self.assertRaises(ValueError, self.books_checker.authors, -1, None, None, None, 'birth_year')

    def test_valid_id_authors(self):
        self.assertRaises(ValueError, self.books_checker.authors, 0, None, None, None, 'title')

    def test_search_text_authors(self):
        #Tests this one parameter works for a valid case
        self.assertEqual(self.books_checker.authors(None, "Ton", None, None, 'title'), [["Toni", "Morrison"],["Toni", "Morrison"]])
        pass

    def test_start_year_authors(self):
        self.assertEqual(self.books_checker.authors(None, None, 1974, None, None), [["Naomi", "Alderman"]])

    def test_end_year_authors(self):
        self.assertEqual(self.books_checker.authors(None, None, None, 1776, None), [["Jane", "Austen"]])

    def test_search_by_birth_year_authors(self):
        self.assertEqual(self.books_checker.authors(None, None, 1945, 1947, "birth_year"), [["Salman", "Rushdie"], ["Connie", "Willis"]])

    def test_search_by_default_authors(self):
        self.assertEqual(self.books_checker.authors(None, None, 1945, 1947, None), [["Salman", "Rushdie"], ["Connie", "Willis"]])

    def test_no_parameters_returns_list_authors(self):
        authorsList = authors(self.books_checker.authors())
        self.assertTrue(authorsList, list)

    def test_no_parameters_returns_dictionaries_authors(self):
        authorsList = authors(self.books_checker.books())
        self.assertTrue(authorsList.get(0), dictionary)

    def test_start_year_too_big_authors(self):
        # test that if we start at year 3000, returns empty list
        assertEqual(self.books_checker.authors(None, None, 3000, None, None), [])

    def test_end_year_too_small_authors(self):
        assertEqual(self.books_checker.authors(None, None, None, 0, None), [])
        pass

    def end_year_before_start_year_authors(self):
        assertEqual(self.books_checker.authors(None, None, 1800, 1700, None), [])
        pass

    # Author function tests

    def test_zero_authors(self):
        self.assertEqual(self.books_checker.author(0), "Willis, Connie")

    def test_negative_authors(self):
        self.assertRaises(ValueError,self.books_checker.author., -1)

    def test_larger_than_max_author(self):
        self.assertRaises(ValueError,self.books_checker.author, 100)
