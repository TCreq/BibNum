#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

import copy #Pour copier différentes listes ou objets
import PyPDF2
import epub as e2
import ebooklib
from ebooklib import epub
import urllib2
import html2text
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://example.com/page.html').read())

txt = soup.find('div', {'class' : 'body'})

print(html2text.html2text(txt))
