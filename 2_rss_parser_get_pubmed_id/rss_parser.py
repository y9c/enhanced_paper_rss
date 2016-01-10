#!/usr/bin/env python
# encoding: utf-8

import urllib
from xml.etree import ElementTree as ET


requestURL = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/erss.cgi?rss_guid=1jEeR5JuI6vIn6cRkj9W4WqO1yytHQtU_SXDimMpc6BLETUEZC'
tree = ET.parse(urllib.urlopen(requestURL))
root = tree.getroot()

pmids = []
for item in root.findall('channel/item'):
    #for title in item.findall('title'):
    #     print title.text
    for guid in item.findall('guid'):
        pmids.append(guid.text.split(':')[1])

f = open('pmid.txt','w')
for pmid in pmids:
    f.write(pmid+'\n')
f.close()
