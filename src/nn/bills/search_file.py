import csv
import sys

with open('strings_to_file.csv','rb') as csvfile:
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        if sys.argv[1] in row[1]:
            print "{}\t{}".format(row[0],row[1])
