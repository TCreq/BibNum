#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#import copy #Pour copier différentes listes ou objets
from PyPDF2 import PdfReader
import epub as e2
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from langdetect import detect
from reportlab.pdfgen import canvas

class Livre():
  
  
  def __init__(self,adresse=None):
    if 'epub' in adresse:
      self.adresse=adresse
      self.book=epub.read_epub(adresse)
      self.book2=e2.open_epub(adresse)
      self.titre=self.book.get_metadata('DC', 'title')[0][0]
      self.auteur=self.book.get_metadata('DC', 'creator')[0][0]
      self.lang=self.book.get_metadata('DC', 'language')[0][0]
      self.table='\n'.join([i.labels[0][0] for i in self.book2.toc.nav_map.nav_point])
      self.t=[i.labels[0][0] for i in self.book2.toc.nav_map.nav_point]
    elif 'pdf' in adresse:
      self.adresse=adresse
      self.book=PdfReader(adresse)
      self.book2=None
      self.titre=str(self.book.metadata.title)
      self.auteur=str(self.book.metadata.author)
      self.lang=detect(self.book.pages[0].extract_text(0))
      self.table='\n'.join(Livre.tablepdf(self.book.outlines))
      self.t=Livre.tablepdf(self.book.outlines)
    else:
      raise Exception("Fichier non reconnu, uniquement fichiers epub ou pdf")

  def tablepdf(l):
    bits=[]
    for i in l:
      if type(i).__name__!='list':
        #bits+=[str(i['/Page']['/Contents'])]
        bits+=[str(i['/Title'])]
      else:
        bits+=['  '+u for u in Livre.tablepdf(i)]
    return bits

  def specpdf(self):
    return [f'titre={self.titre}',f'auteur={self.auteur}',f'langue={self.lang}',f'Table des matières : ',]+[str(i) for i in self.t]

  def __repr__(self):
    return ('\n'+60*'-'+'\n').join([f'titre={self.titre}',f'auteur={self.auteur}',f'langue={self.lang}',f'Table des matières : \n'+self.table])



l=Livre('stendhal_-_le_rouge_et_le_noir.epub')
print(l)
#l=Livre('stendhal_le_rouge_et_le_noir.pdf')
#print(l)





with open("rapport.txt","w") as f:
  print(str(l), file=f)


'''
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
'''

"""
book = epub.EpubBook()
book.set_identifier('rapport'+l.titre)
book.set_title(l.titre)
book.set_language(l.lang)
book.add_author(l.auteur)
soup=BeautifulSoup()
body=soup.new_tag('body')
soup.insert(0,body)
s=l.specpdf()
s.reverse()
for line in s:
  body.insert(0,line)
# intro chapter
c1 = epub.EpubHtml(title='Rapport',
                   file_name='Rapport.xhtml',
                   lang='fr')
c1.set_content(soup.prettify())
#print(c1.get_content())
book.add_item(c1)
style = 'body { font-family: Times, Times New Roman, serif; }'

nav_css = epub.EpubItem(uid="style_nav",
                        file_name="style/nav.css",
                        media_type="text/css",
                        content=style)
book.add_item(nav_css)
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())
epub.write_epub('test.epub', book)




with open('rapport.html', 'w') as outfile:
    outfile.write(soup.prettify())
"""

book = epub.EpubBook()
book.set_identifier('sample123456')
book.set_title('Sample book')
book.set_language('en')

book.add_author('Aleksandar Erkalovic')
book.add_metadata('DC', 'description', 'This is description for my book')
book.add_metadata(None, 'meta', '', {'name': 'key', 'content': 'value'})

# intro chapter
c1 = epub.EpubHtml(title='Introduction',
                   file_name='intro.xhtml',
                   lang='en')
c1.set_content(u'<html><body><h1>Introduction</h1><p>Introduction paragraph.</p></body></html>')

# about chapter
c2 = epub.EpubHtml(title='About this book',
                   file_name='about.xhtml')
c2.set_content('<h1>About this book</h1><p>This is a book.</p>')


#print(c1.get_content())


book.add_item(c1)
book.add_item(c2)

style = 'body { font-family: Times, Times New Roman, serif; }'

nav_css = epub.EpubItem(uid="style_nav",
                        file_name="style/nav.css",
                        media_type="text/css",
                        content=style)
book.add_item(nav_css)

book.toc = (epub.Link('intro.xhtml', 'Introduction', 'intro'),
              (
                epub.Section('Languages'),
                (c1, c2)
              )
            )
book.spine = ['nav', c1, c2]

book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

epub.write_epub('test.epub', book)





































