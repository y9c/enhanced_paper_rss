#!/usr/bin/env python
# encoding: utf-8

import urllib
from xml.etree import ElementTree as ET

feedurl = 'http://www.ncbi.nlm.nih.gov/entrez/eutils/erss.cgi?rss_guid=1jEeR5JuI6vIn6cRkj9W4WqO1yytHQtU_SXDimMpc6BLETUEZC'

def fetch_pmid(requestURL):
    root = ET.parse(urllib.urlopen(requestURL)).getroot()
    pmids = []
    for item in root.findall('channel/item'):
        for guid in item.findall('guid'):
            pmids.append(guid.text.split(':')[1])
    return pmids


def pmids2dois(pmids):
    dois=[]
    requestURL = 'http://www.zhaowenxian.com/?q=' + ','.join(pmids)
    print urllib.urlopen(requestURL)
    root = ET.parse(urllib.urlopen(requestURL)).getroot()
    for atype in root.findall('record'):
        dois.append(atype.get('doi'))
    return dois

dois = pmids2dois(fetch_pmid(feedurl))
f = open('dois.txt', 'w')
for doi in dois:
    if doi != None:
        f.write(doi+'\n')
