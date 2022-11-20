#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#import copy #Pour copier différentes listes ou objets
#import PyPDF2
import epub as e2
#import ebooklib
from ebooklib import epub
#from bs4 import BeautifulSoup


class Livre():
  
  
  def __init__(self,adresse=None):
    if adresse==None:
      self.book=None
      self.book2=None
      self.titre=''
      self.auteur=''
      self.lang=''
      self.table=''
    else:
      self.book=epub.read_epub(adresse)
      self.book2=e2.open_epub(adresse)
      self.titre=self.book.get_metadata('DC', 'title')[0][0]
      self.auteur=self.book.get_metadata('DC', 'creator')[0][0]
      self.lang=self.book.get_metadata('DC', 'language')[0][0]
      self.table='\n'.join([i.labels[0][0] for i in self.book2.toc.nav_map.nav_point])
  
  def __repr__(self):
    return ('\n'+60*'-'+'\n').join([f'titre={self.titre}',f'auteur={self.auteur}',f'langue={self.lang}',f'Table des matières : \n'+self.table])



l=Livre('stendhal_-_le_rouge_et_le_noir.epub')
print(l)



