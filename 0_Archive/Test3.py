#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

import copy #Pour copier différentes listes ou objets
import PyPDF2
import epub as e2
import ebooklib
from ebooklib import epub
import csv
import requests
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString

from io import StringIO
from xml.dom.minidom import parseString
e = parseString('<foo/>')
out = StringIO()
e.writexml(out)
s = out.getvalue()
print(s)
dom = parseString(s)
print(dom)
e2 = parseString(s)
print(e2)

### ----------------------------------------------------------

#book=e2.open_epub('stendhal_-_le_rouge_et_le_noir.epub')

#xmlfile=book.toc.as_xml_document()

'''
### -----------------------------------------------------------

book = epub.read_epub('stendhal_-_le_rouge_et_le_noir.epub')

print(book.get_metadata('DC', 'title')[0][0])
#[('Ratio', {})]
print(book.get_metadata('DC', 'creator')[0][0])
#[('Firstname Lastname ', {})]
print(book.get_metadata('DC', 'language')[0][0])


#cover_image = book.get_item_with_id('cover-image')
#print(cover_image) #None
#index = book.get_item_with_href('index.xhtml')
#print(index) #None

#print(book.metadata)

book=e2.open_epub('stendhal_-_le_rouge_et_le_noir.epub')

t=book.toc.as_xml_document()
print(t)





'''
