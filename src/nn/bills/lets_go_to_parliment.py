# -*- coding: utf8 -*-
import xml.etree.ElementTree as ET
import os
for file in os.listdir('debates'):
    if '.xml' in file and '.xml.' not in file:
        tree = ET.parse('debates/{}'.format(file))
        root = tree.getroot()
        for thing in root:
            if thing.text == None:
                continue
            ip = thing.text.encode('ascii','ignore')
            if ip.strip() != '':
                print "{}\t{}".format(file,ip.translate(None, '\n\t\u'))
