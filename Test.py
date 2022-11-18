#!/bin/env python3

### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

import copy #Pour copier différentes listes ou objets
import PyPDF2
import epub

### Definition de la classe et des fonctions de la classe


book = epub.open_epub('stendhal_-_le_rouge_et_le_noir.epub')


opf0=book.opf
meta=opf0.metadata
# meta est un objet de la classe Metadata contenant plusieurs titres
title=meta.titles[0][0]
print(f"le titre du livre est : {title}")


toc0=book.toc
print(toc0.authors)
print(toc0.__class__.__name__)
print(toc0.nav_map)
#print(toc0.nav_map.nav_point)
print("stop")
#print(i.class_name for i in toc0.nav_map.nav_point)




k=0
for item_id, linear in book.opf.spine.itemrefs:
    k+=1
    item = book.get_item(item_id)
    # Check if linear or not
    if linear:
        #print('Linear item "%s"' % item.href)
        pass
    else:
        #print('Non-linear item "%s"' % item.href)
        pass
    # read the content
    data = book.read_item(item)
    if k==3 :
        #print(data)
        pass



#print(book.opf.spine.itemrefs[0])