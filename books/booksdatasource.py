'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018
    Modified by Eric Alexander, April 2019
    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class.
    
    Methods implemented by Ginnie White and Kate Grossman
'''
import csv

class BooksDataSource:
    '''
    A BooksDataSource object provides access to data about books and authors.
    The particular form in which the books and authors are stored will
    depend on the context (i.e. on the particular assignment you're
    working on at the time).
    Most of this class's methods return Python lists, dictionaries, or
    strings representing books, authors, and related information.
    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):
        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}
    For a living author, the death_year is represented in the author's
    Python dictionary as None.
        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}
    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.
    A book is represented as a dictionary with the keys 'id', 'title',
    and 'pu'\'ar'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:
        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}
    '''


    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        ''' Initializes this data source from the three specified  CSV files, whose
            CSV fields are:
                books: ID,title,publication-year
                  e.g. 6,Good Omens,1990
                       41,Middlemarch,1871
                authors: ID,last-name,first-name,birth-year,death-year
                  e.g. 5,Gaiman,Neil,1960,NULL
                       6,Pratchett,Terry,1948,2015
                       22,Eliot,George,1819,1880
                link between books and authors: book_id,author_id
                  e.g. 41,22
                       6,5
                       6,6
                  [that is, book 41 was written by author 22, while book 6
                    was written by both author 5 and author 6]
            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.
            NOTE TO STUDENTS: I have not specified how you will store the books/authors
            data in a BooksDataSource object. That will be up to you, in Phase 3.
        '''
	# Create all instance variables needed in the class
        self.create_booksList()
        self.create_authorsList()
        self.create_linkList()

        self.create_author_list_of_Dict()
        self.create_book_list_of_Dict()
        self.create_link_list_of_Dict()


    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment
            for a description of how a book is represented.)
            Raises ValueError if book_id is not a valid book ID.
        '''
        if int(book_id) < 0 or int(book_id) > len(self.book_list_of_Dict):
            raise ValueError("The ID is out of range.")
        else:
            requested_book = self.book_list_of_Dict[int(book_id)]
            return(requested_book)


    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of
            the specified non-None criteria.
                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year
            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.
            The list of books is sorted in an order depending on the sort_by parameter:
                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year
            See the BooksDataSource comment for a description of how a book is represented.
            QUESTION: Should Python interfaces specify TypeError?
            Raises TypeError if author_id, start_year, or end_year is non-None but not an integer.
            Raises TypeError if search_text or sort_by is non-None, but not a string.
				OUR ANSWER: Not for this assignment.
            QUESTION: How about ValueError? And if so, for which parameters?
            Raises ValueError if author_id is non-None but is not a valid author ID.
				OUR ANSWER: Yes, but just for author_id.
        '''

        if sort_by == 'year':
            sorted_books = sorted(self.book_list_of_Dict, key = lambda i: i["publication_year"])
        else:
            sorted_books = sorted(self.book_list_of_Dict, key = lambda i: i["title"])

        author_id_list = []
        # Apply author_id parameter to list
        if author_id != None:
            if int(author_id) < 0 or int(author_id) > len(self.author_list_of_Dict):
                raise ValueError

            book_id_list = []
            for item in self.link_list_of_Dict:
                for key in item:
                    if int(item.get(key)) == int(author_id):
                        book_id_list.append(key)
            for book in sorted_books:
                if book.get('id') in book_id_list:
                    author_id_list.append(book)
        else:
            author_id_list = sorted_books

        search_text_list = []
        # Apply serch_text parameter to list
        if search_text != None:
            case_insensitive_seach_text_books = search_text.lower()

            for book in author_id_list:
                lower_dict = self.lower_case_dict(book)
                if case_insensitive_seach_text_books in lower_dict.get('title'):
                    search_text_list.append(book)
        else:
            search_text_list = author_id_list

        start_year_list = []
        # Apply start_year parameter to list
        if start_year != None:
            for book in search_text_list:
                if int(book.get('publication_year')) >= int(start_year):
                    start_year_list.append(book)
        else:
            start_year_list = search_text_list

        end_year_list = []
        # Apply end_year parameter to list
        if end_year != None:
            for book in start_year_list:
                if int(book.get('publication_year')) <= int(end_year):
                    end_year_list.append(book)
        else:
            end_year_list = start_year_list
        if start_year != None and end_year != None and int(end_year) < int(start_year):
            end_year_list = []

        return end_year_list

    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.)
            Raises ValueError if author_id is not a valid author ID.
        '''
        if int(author_id) < 0 or int(author_id) > len(self.author_list_of_Dict):
            raise ValueError("The ID is out of range.")
        else:
            requested_author = self.author_list_of_Dict[int(author_id)]
            return(requested_author)

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.
                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year
            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.
            The list of authors is sorted in an order depending on the sort_by parameter:
                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year
            See the BooksDataSource comment for a description of how an author is represented.
        '''
        if sort_by == 'last_name':
            sorted_authors = sorted(self.author_list_of_Dict, key = lambda i:
            (i["last_name"], i['first_name'], i['birth_year']))
        else:
            sorted_authors = sorted(self.author_list_of_Dict, key = lambda i:
            (i["birth_year"], i["last_name"], i["first_name"]))


        book_id_list = []
        # Apply book_id parameter to list
        if book_id != None:
            if int(book_id) < 0 or int(book_id) > len(self.book_list_of_Dict):
                raise ValueError
                print("Value error detected")
            author_id_list = []
            for item in self.link_list_of_Dict:
                if book_id in item.keys():
                    author_id_list.append(item.get(book_id))

            for book in sorted_authors:
                if book.get('id') in author_id_list:
                    book_id_list.append(book)
        else:
            book_id_list = sorted_authors

        search_text_authors_list = []
        # Apply search_text parameter to list.
        if search_text != None:
            case_insensitive_seach_text_author = search_text.lower()
            for book in book_id_list:
                lower_dict = self.lower_case_dict(book)
                if search_text in book.get('first_name') or search_text in book.get('last_name'):
                    search_text_authors_list.append(book)
        else:
            search_text_authors_list = book_id_list

        start_year_authors_list = []
        # Apply start_year parameter to list
        if start_year != None:
            for book in search_text_authors_list:
                if book.get('death_year') != "NULL" and int(book.get('death_year')) >= int(start_year):
                    start_year_authors_list.append(book)
                if int(book.get('birth_year')) >= int(start_year):
                    start_year_authors_list.append(book)
                if book.get('death_year') == "NULL" and int(book.get('birth_year')) <= int(start_year):
                    start_year_authors_list.append(book)
                if int(start_year) > 2019:
                    start_year_authors_list = []
        else:
            start_year_authors_list = search_text_authors_list

        end_year_authors_list = []
        # Apply start_year end_year parameters to list
        if end_year != None:
            for book in start_year_authors_list:
                if book.get('death_year')!= "NULL" and int(book.get('birth_year')) <= int(end_year):
                    end_year_authors_list.append(book)
        else:
            end_year_authors_list = start_year_authors_list
        if start_year != None and end_year != None and int(end_year) < int(start_year):
            end_year_authors_list = []


        return end_year_authors_list

    # Methods that convert csv files to lists

    def create_booksList(self):
        self.booksList=[]
        with open('books.csv', "r") as csvfile:
            reader = csv.reader(csvfile)

            for book in reader:
                self.booksList.append(book)

        return self.booksList

    def create_authorsList(self):
        self.authorsList = []
        with open('authors.csv', "r") as csvfile:
            reader = csv.reader(csvfile)

            for author in reader:
                self.authorsList.append(author)

    def create_linkList(self):
        self.linkList=[]
        with open('books_authors.csv', "r") as csvfile:
            reader = csv.reader(csvfile)

            for id in reader:
                self.linkList.append(id)

        return self.linkList

    # Convert list of rows to list of dictionaries

    def create_author_list_of_Dict(self):
        self.author_list_of_Dict = []
        for item in self.authorsList:
            dict = {
            'id': item[0], 'last_name': item[1], 'first_name': item[2],
            'birth_year': item[3], 'death_year': item[4]
            }
            self.author_list_of_Dict.append(dict)

    def create_book_list_of_Dict(self):
        self.book_list_of_Dict=[]
        for item in self.booksList:
            dict = {
            "id": item[0],
            "title": item[1],
            "publication_year": item[2],
            }
            self.book_list_of_Dict.append(dict)
        return self.book_list_of_Dict

    def create_link_list_of_Dict(self):
        self.link_list_of_Dict=[]
        for item in self.linkList:
            dict = {
            item[0]: item[1],
            }
            self.link_list_of_Dict.append(dict)
        return self.link_list_of_Dict

    # Turn all keys in dictionary to lower case    
    def lower_case_dict(self, dictionary):
        new_dict = dict((k.lower(), v.lower()) for k, v in dictionary.items())
        return new_dict


# Test object created for our own use
if __name__ == '__main__':
    test = BooksDataSource("books.csv", "authors.csv", "books_authors.csv")
