import csv
import sys

data = {}

with open(sys.argv[1], 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    # get first line
    for row in reader:
        data[row['rowid']] = row

for i in data.keys():
    print data[i]['Bill']
