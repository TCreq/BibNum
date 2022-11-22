#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#import copy #Pour copier différentes listes ou objets
import sys
from Livre import Livre,Corpus
from glob import glob

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas

### -------------------------------------------------------------------------------------------
### Recuperation des arguments ###

args=sys.argv
#print(args)

### ---------------------------------------------------------------------------------------------
### Configuration des Repertoires de lecture, ecriture, log ###

config='bibli.conf'

# exemple d'entrée : ./bibli.py -c bibli2.conf update
if '-c' in args:
  config=args[args.index('-c')+1]
  #print(f'{config=}')

archive=''
rapports=''
log=''

il = 0
with open(config,"r") as f:
  for line in f:
    il += 1
    #print(f"{il:03d}: {line}", end="")
    if il==1:
      archive=line.strip()
      if archive[-1]!="/":
        archive+="/"
    elif il==2:
      rapports=line.strip()
    elif il==3:
      log=line.strip()

print(f'{archive=}')
print(f'{rapports=}')
print(f'{log=}')

###--------------------------------------------------------------------------------------

files=glob(archive+'*')
print(files)

#c=Corpus(files)
#print(c)

###--------------------------------------------------------------------------------------

if 'init' in args:
  print('init')

if 'update' in args:
  print('update')


###--------------------------------------------------------------------------------------


l=Livre('stendhal_-_le_rouge_et_le_noir.epub')
print(l)
#l=Livre('stendhal_le_rouge_et_le_noir.pdf')
#print(l)

### Rapport TXT
with open("rapport.txt","w") as f:
  print(str(l), file=f)


### Rapport PDF
my_canvas = canvas.Canvas("rapport.pdf")
k=0
for i in l.specpdf():
  my_canvas.drawString(100, 750-k*15, str(i))
  if 750-k*15<100:
    my_canvas.showPage()
    k=0
  k+=1
my_canvas.showPage()
my_canvas.save()


### Rapport Epub
book = epub.EpubBook()
book.set_identifier('rapportLivre1')
book.set_title('RapportLivre')
book.set_language('fr')
book.add_author('system')
book.add_metadata('DC', 'description', 'Rapport sur le livre')
book.add_metadata(None, 'meta', '', {'name': 'key', 'content': 'value'})
c1 = epub.EpubHtml(title='Proprietes',
                   file_name='prop.xhtml',
                   lang='fr')
c1.set_content('<html><body><h1>Propietes</h1><p>'+str(l)+'</p></body></html>')
c2 = epub.EpubHtml(title='Fin',
                   file_name='fin.xhtml')
c2.set_content('<h1> ... </h1><p> ... </p>')
book.add_item(c1)
book.add_item(c2)
style = 'body { font-family: Times, Times New Roman, serif; }'
nav_css = epub.EpubItem(uid="style_nav",
                        file_name="style/nav.css",
                        media_type="text/css",
                        content=style)
book.add_item(nav_css)
book.toc = (c1,c2)
book.spine = ['nav', c1, c2]
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
epub.write_epub('rapport.epub', book)













































