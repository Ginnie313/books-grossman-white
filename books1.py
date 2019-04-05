'''
Testing some things
'''
import sys
import csv


input_file = sys.argv[1] #probably want a file not found error here somewhere
rows = []
#read csv file
with open(input_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows.append(row)

action = sys.argv[2]
if action != "books" and action != "authors":
    print('Usage: Action must be "books" or "authors"', file=sys.stderr)

try:
    sort_direction = sys.argv[3]
except:
    sort_direction = "forward"

if sort_direction != "forward" and sort_direction != "reverse":
    print('Usage: Action must be "forward", "reverse" or nothing', file=sys.stderr)


#def sort(action, sort_direction)
