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


def main():

    input_file = sys.argv[1]

    rows = []
    #read csv file
    try:
        with open(input_file, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                rows.append(row)
    except:
        print("Usage: File not found", file=sys.stderr)

    try:
        action = sys.argv[2]
        if action != "books" and action != "authors":
            print('Usage: Action must be "books" or "authors"', file=sys.stderr)
    except:
        print("Usage: Need a third argument action")

    try:
        sort_direction = sys.argv[3]
    except:
        sort_direction = "forward"

    if sort_direction != "forward" and sort_direction != "reverse":
        print("Usage: Action must be forward, reverse")
        print("or nothing", file=sys.stderr)

    if action == "books":
        sortByBook(rows, sort_direction)

    if action == "authors":
        sortByAuthor(rows, sort_direction)

def sortByBook(rows, sort_direction):
    booklist = []
    for row in rows:
        booklist.append(row[0])

    booklist.sort()

    if sort_direction == "reverse":
        list.reverse(booklist)

    for item in booklist:
        print(item)


def sortByAuthor(rows, sort_direction):
    authorlist = []
    for row in rows:
        item = row[2]
        newitem = re.findall("[^0-9()\-\s]+", item)
        authorlist.append(newitem)
    authorlist.sort(key=takeLast)
    if sort_direction == "reverse":
        authorlist.reverse()
    for item in authorlist:
        print(*item)

def takeLast(elem):
    if "and" in elem:
        andIndex = elem.index("and") -1
        return elem[andIndex][0]
    else:
        return elem[-1][0]

if __name__ == '__main__':
    main()
