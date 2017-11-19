import csv

with open('../to_get.txt','rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print "https://www.theyworkforyou.com/pwdata/scrapedxml/debates/"+row[1]
