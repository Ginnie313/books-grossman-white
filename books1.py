'''
books1.py
Kate Grossman and Ginnie White, 8 March 2019

A program that implements sorting a csv file by author and by book title
(both forwards and backwards) from the command line.

Credit to Danny Maya for helping with string stripping line
'''

import sys
import csv
import re

# This is the main function that calls sub functions to implement author sort
# and book sort.
def main():

    input_file = sys.argv[1]

    rows = []

    # This reads the csv file and throws an error if file not found.
    try:
        with open(input_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                rows.append(row)
    except:
        print("Usage: File not found", file=sys.stderr)

    # This gets the action and returns an error if the action is invalid.
    try:
        action = sys.argv[2]
        if action != "books" and action != "authors":
            print('Usage: Action must be "books" or "authors"', file=sys.stderr)
    except:
        # Action is invalid if user did not input "books" or "authors".
        action = "invalid"
        print("Usage: Need a third argument action", file=sys.stderr)

    # If there is no sort_direction given, sort_direction is forward.
    try:
        sort_direction = sys.argv[3]
    except:
        sort_direction = "forward"

    # If sort_direction is invalid, throw a usage error.
    if sort_direction != "forward" and sort_direction != "reverse":
        print("Usage: Action must be forward, reverse")
        print("or nothing", file=sys.stderr)

    # If the user wants to sort by books, call sortByBook.
    if action == "books":
        sortByBook(rows, sort_direction)

    # If the user wants to sort by authors, call sortByAuthor.
    if action == "authors":
        sortByAuthor(rows, sort_direction)

# This sorts by book title. It takes in a list of everything in the csv File
# and String sort_direction, then prints out sorted book titles.
def sortByBook(rows, sort_direction):
    booklist = []
    for row in rows:
        booklist.append(row[0])

    booklist.sort()

    if sort_direction == "reverse":
        list.reverse(booklist)

    for item in booklist:
        print(item)

# This sorts by author's last name. It takes in a list of everything in the csv
# File and String sort_direction, then prints out sorted author names.
def sortByAuthor(rows, sort_direction):
    authorlist = []
    for row in rows:
        item = row[2]
        # This strips all dates from author names.
        newitem = re.findall("[^0-9()\-\s]+", item)
        authorlist.append(newitem)
    # We use the function takeLast to get the last element in each row.
    authorlist.sort(key=takeLast)
    if sort_direction == "reverse":
        authorlist.reverse()
    for item in authorlist:
        print(*item)

# This is a function that gets the last element in a row, but if the row
# contains "and", the function finds the first element before "and".
def takeLast(elem):
    if "and" in elem:
        andIndex = elem.index("and") -1
        return elem[andIndex][0]
    else:
        return elem[-1][0]

if __name__ == '__main__':
    main()
