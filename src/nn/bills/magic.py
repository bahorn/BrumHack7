import csv
import sys
import os
import numpy as np
import xml.etree.ElementTree as ET
import json

everything = []
words = eval(open('words').read())
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        all = []
        for i in row:
            if 'mpid' in i:
                b = int(row[i])
                if b == 1 or b == 2:
                    all += [1.0]
                elif b == 3:
                    all += [0.5]
                else:
                    all += [0.0]
        #print {'bill':row['Bill'],'all':all}
        infiles = []
        doc = [0 for i in range(len(words))]
        c = 0.0
        for x in os.listdir('debates/'):
            if row['date'] in x and '.xml' in x and '.xml.' not in x:
                #print "{}\t{}".format(x,row['Bill'])
                tree = ET.parse('debates/'+x)
                root = tree.getroot()
                for y in root:
                    if y.text == None:
                        continue
                    d = y.text.encode('ascii','ignore')
                    for line in d.split('\n')[:-1]:
                        for word in line.split(' '):
                            w = ''.join(e for e in word if e.isalnum())
                            for j in range(len(words)):
                                if words[j] == w.lower():
                                    doc[j] += 1
                                    c += 1
        if doc == [0 for i in range(len(words))]:
            f = open('/dev/stderr','a')
            f.write('{}\n'.format(x))
            f.close()
        else:
            for i in range(len(doc)):
                doc[i] = doc[i]/c
        
        everything += [{'bill':row['Bill'],'in':doc,'out':all}]
        #print infiles

f = open('../data_for_everything','w')
f.write(json.dumps(everything))
f.close()
