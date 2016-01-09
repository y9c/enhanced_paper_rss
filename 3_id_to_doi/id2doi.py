#!/usr/bin/env python
# encoding: utf-8

import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('http://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?ids=23193288').getroot()

import urllib
from xml.etree import ElementTree as ET

show = 'heroes'
season = '4'
language = 'en'
limit = '1'

requestURL = 'http://api.allsubs.org/index.php?' \
                   + 'search=' + show \
                              + '+season+' + season \
                                         + '&language=' + language \
                                                    + '&limit=' + limit

                                                    root = ET.parse(urllib.urlopen(requestURL)).getroot()


