import sys
import numpy as np
import xml.etree.ElementTree as ET

tree = ET.parse(sys.argv[1])
root = tree.getroot()
words = eval(open('words').read())
doc = [0 for i in range(len(words))]
c = 0.0
for thing in root:
    if thing.text == None:
        continue
    d = thing.text.encode('ascii','ignore')
    for line in d.split('\n')[:-1]:
        for word in line.split(' '):
            w = ''.join(e for e in word if e.isalnum())
            for j in range(len(words)):
                if words[j] == w.lower():
                    doc[j] += 1
                    c += 1
if doc == [0 for i in range(len(words))]:
    #print "FUCK",sys.argv[1]
    pass
    f = open('/dev/stderr','a')
    f.write('{}\n'.format(sys.argv[1]))
else:
    for i in range(len(doc)):
        doc[i] = doc[i]/c
    print doc
