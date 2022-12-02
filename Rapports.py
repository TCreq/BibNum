#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#import copy #Pour copier différentes listes ou objets
from Livre import Livre,Corpus
import ebooklib
from ebooklib import epub
from reportlab.pdfgen import canvas
import logging

### Rapport TXT
def change(titre):
  return titre.replace(' ','_').replace('\\','_').replace("'","_").replace("-","_").replace("/","_")
def RTXT(l,rapports,i='0'):
  """ fonction du rapport txt contenant la table des matieres """
  adresse=str(rapports+str(i)+"_"+change(l.titre)+"_r.txt").replace(' ','_')
  with open(adresse,"w") as f:
    print(str(l), file=f)
  logging.info("Ajout de "+adresse)
### Rapport PDF
def RPDF(l,rapports,i='0'):
  """ fonction du rapport pdf contenant la table des matieres """
  adresse=str(rapports+str(i)+"_"+change(l.titre)+"_r.pdf")
  my_canvas = canvas.Canvas(adresse)
  k=0
  for u in l.specpdf():
    my_canvas.drawString(65, 750-k*15, str(u))
    if 750-k*15<100:
      my_canvas.showPage()
      k=0
    k+=1
  my_canvas.showPage()
  my_canvas.save()
  logging.info(f"Ajout de "+adresse)

### Rapport Epub
def REPUB(l,rapports,i='0'):
  """ fonction du rapport epub contenant la table des matieres """
  book = epub.EpubBook()
  book.set_identifier('rapport '+l.titre)
  book.set_title('Rapport - '+l.titre)
  book.set_language('fr')
  book.add_author('system')
  book.add_metadata('DC', 'description', 'Rapport sur le livre')
  book.add_metadata(None, 'meta', '', {'name': 'key', 'content': 'value'})
  c1 = epub.EpubHtml(title='Table des matieres',
                   file_name='prop.xhtml',
                   lang='fr')
  c1.set_content('<html><body><h1>Table des Matieres</h1><p>'+l.specepub()+'</p></body></html>')
  c2 = epub.EpubHtml(title='...',
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
  adresse=str(rapports+str(i)+"_"+change(l.titre)+"_r.epub")
  epub.write_epub(adresse, book)
  logging.info(f"Ajout de "+adresse)

def Tables(c,rapports):
  """ fonction qui génère les rapports de table des matieres pour chaque livre du corpus """
  k=0
  for l in c:
    RTXT(l,rapports,k)
    RPDF(l,rapports,k)
    REPUB(l,rapports,k)
    k+=1


### Liste des Ouvrages ---------------------------------------------
# la liste des ouvrages (au format texte, PDF et epub)
# qui contient pour chaque livre son titre, son auteur,
# la langue et le nom du fichier correspondant

def Ouvrages(c,rapports):
  """ fonction qui génère les 3 rapports pour le corpus sur la liste des ouvrages """
  lprops=[]
  for i in c:
    lprops+=i.props()+["_______________________________"," "]
  texte="\n".join(lprops)
  tepub='<br />'.join(lprops)
  #print(texte)
  ## Rapport Ouvrages TXT
  with open(rapports+"ouvrages.txt","w") as f:
    print(texte, file=f)
  logging.info(f"Ajout de "+rapports+"ouvrages.txt")
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
  logging.info(f"Ajout de "+rapports+"ouvrages.pdf")
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
  logging.info(f"Ajout de "+rapports+"ouvrages.epub")


### Liste des Auteurs
# la liste des auteurs (au format texte, PDF et epub)
# contenant pour chacun d’eux les titres de ses livres
# et le nom des fichiers associés.

def Auteurs(c,rapports):
  """ fonction qui génère les rapports sur les auteurs du corpus """
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
  logging.info(f"Ajout de "+rapports+"auteurs.txt")
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
  logging.info(f"Ajout de "+rapports+"auteurs.pdf")
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
  logging.info(f"Ajout de "+rapports+"auteurs.epub")
































