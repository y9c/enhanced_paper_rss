#!/usr/bin/env python
# encoding: utf-8

import urllib
from xml.etree import ElementTree as ET

ids = ['23193288', '23193284', '23193289', '23193238']
dois=[]

requestURL = 'http://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=' + ','.join(ids)
root = ET.parse(urllib.urlopen(requestURL)).getroot()
for atype in root.findall('record'):
    dois.append(atype.get('doi'))

f = open('dois.txt', 'w')
for doi in dois:
    if doi != None:
        f.write(doi+'\n')
