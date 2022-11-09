#!/bin/env python3

### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

import copy #Pour copier différentes listes ou objets
import PyPDF2
import epub

### Definition de la classe et des fonctions de la classe


book = epub.open_epub('stendhal_-_le_rouge_et_le_noir.epub')

for item_id, linear in book.opf.spine.itemrefs:
    item = book.get_item(item_id)
    # Check if linear or not
    if linear:
        print('Linear item "%s"' % item.href)
    else:
        print('Non-linear item "%s"' % item.href)
    # read the content
    data = book.read_item(item)