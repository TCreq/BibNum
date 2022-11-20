#!/bin/env python3

### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

import copy #Pour copier différentes listes ou objets
import PyPDF2
import ebooklib
from ebooklib import epub

### Definition de la classe et des fonctions de la classe


book = epub.read_epub('stendhal_-_le_rouge_et_le_noir.epub')

t1=book.get_metadata('DC', 'title')[0][0]
print(t1)

t2=book.get_metadata('DC', 'creator')[0][0]
print(t2)

#t3=book.get_metadata('DC', 'identifier')
#print(t3)

for item in book.get_items():
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        print('==================================')
        print('NAME : ', item.get_name())
        print('----------------------------------')
        print(item.get_content())
        print('==================================')













