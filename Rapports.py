#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#import copy #Pour copier différentes listes ou objets
from Livre import Livre,Corpus
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas

### Rapport TXT
def RTXT(l,rapports):
  with open(rapports+"rapport.txt","w") as f:
    print(str(l), file=f)

### Rapport PDF
def RPDF(l,rapports):
  my_canvas = canvas.Canvas(rapports+"rapport.pdf")
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
def REpub(l,rapports):
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
  c1.set_content('<html><body><h1>Propietes</h1><p>'+l.specepub()+'</p></body></html>')
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
  epub.write_epub(rapports+'rapport.epub', book)



### Liste des Ouvrages ---------------------------------------------
# la liste des ouvrages (au format texte, PDF et epub)
# qui contient pour chaque livre son titre, son auteur,
# la langue et le nom du fichier correspondant

def Ouvrages(c,rapports):
  lprops=[]
  for i in c:
    lprops+=i.props()+["_______________________________"," "]
  texte="\n".join(lprops)
  tepub='<br />'.join(lprops)
  #print(texte)
  ## Rapport Ouvrages TXT
  with open(rapports+"ouvrages.txt","w") as f:
    print(texte, file=f)
  ## Rapport Ouvrages PDF
  my_canvas = canvas.Canvas(rapports+"ouvrages.pdf")
  k=0
  for i in lprops:
    my_canvas.drawString(65, 750-k*15, str(i))
    if 750-k*15<100:
      my_canvas.showPage()
      k=0
    k+=1
  my_canvas.showPage()
  my_canvas.save()
  ##Rapport Ouvrages EPUB
  book = epub.EpubBook()
  book.set_identifier('Ouvrages')
  book.set_title('Ouvrages')
  book.set_language('fr')
  book.add_author('system')
  book.add_metadata('DC', 'description', 'Ouvrages de la bibliotheque')
  book.add_metadata(None, 'meta', '', {'name': 'key', 'content': 'value'})
  c1 = epub.EpubHtml(title='Ouvrages',
                 file_name='prop.xhtml',
                 lang='fr')
  c1.set_content('<html><body><h1>Ouvrages</h1><p>'+tepub+'</p></body></html>')
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
  epub.write_epub(rapports+'ouvrages.epub', book)


### Liste des Auteurs
# la liste des auteurs (au format texte, PDF et epub)
# contenant pour chacun d’eux les titres de ses livres
# et le nom des fichiers associés.

def Auteurs(c,rapports):
  loeuvres=c.nombre()*['']
  k=0
  for i in c:
    loeuvres[k]=" ".join(i.auth())
    k+=1
  loeuvres.sort(key=str.lower)

  texte="\n".join(loeuvres)
  taepub='<br />'.join(loeuvres)
  #print(texte)
  ## Rapport Auteurs TXT
  with open(rapports+"auteurs.txt","w") as f:
    print(texte, file=f)
  ## Rapport Auteurs PDF
  my_canvas = canvas.Canvas(rapports+"auteurs.pdf")
  k=0
  for i in loeuvres:
    my_canvas.drawString(65, 750-k*15, str(i))
    if 750-k*15<100:
      my_canvas.showPage()
      k=0
    k+=1
  my_canvas.showPage()
  my_canvas.save()
  ## Rapport Auteurs EPUB
  book = epub.EpubBook()
  book.set_identifier('Auteurs')
  book.set_title('Auteurs')
  book.set_language('fr')
  book.add_author('system')
  book.add_metadata('DC', 'description', 'Liste des Auteurs')
  book.add_metadata(None, 'meta', '', {'name': 'key', 'content': 'value'})
  c1 = epub.EpubHtml(title='Auteurs',
                 file_name='prop.xhtml',
                 lang='fr')
  c1.set_content('<html><body><h1>Auteurs</h1><p>'+taepub+'</p></body></html>')
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
  epub.write_epub(rapports+'auteurs.epub', book)

































