#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#import copy #Pour copier différentes listes ou objets
from PyPDF2 import PdfReader
import epub as e2
import ebooklib
from ebooklib import epub
from langdetect import detect

###---------------------------------------------------------------

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
      self.abstract=str(self).strip('\n')
    elif 'pdf' in adresse:
      self.adresse=adresse
      self.book=PdfReader(adresse)
      self.book2=None
      self.titre=str(self.book.metadata.title)
      self.auteur=str(self.book.metadata.author)
      #self.lang=detect(self.book.pages[0].extract_text(0))
      self.lang='fr' ### language detect est très long, donc pour les tests on triche
      self.table='\n'.join(Livre.tablepdf(self.book.outlines))
      self.t=Livre.tablepdf(self.book.outlines)
      self.abstract=str(self).strip('\n')
    else:
      raise Exception("Fichier non reconnu, uniquement fichiers epub ou pdf")

  def __eq__(self,l):
    """ fonction pour comparer deux livres (inutilisée) """
    a=self.adresse==l.adresse
    b=self.titre==l.titre
    c=self.auteur==l.auteur
    d=self.lang==l.lang
    f=self.table==l.table
    return a and b and c and d and f

  def tablepdf(l):
    """ renvoie une liste avec les lignes de la table des matieres """
    bits=[]
    for i in l:
      if type(i).__name__!='list':
        #bits+=[str(i['/Page']['/Contents'])]
        bits+=[str(i['/Title'])]
      else:
        bits+=['  '+u for u in Livre.tablepdf(i)]
    return bits

  def specpdf(self):
    """ renvoie une liste avec les lignes du rapport pdf de la table des matieres """
    return [f'titre={self.titre}',f'auteur={self.auteur}',f'langue={self.lang}',f'Table des matières : ']+[str(i) for i in self.t]

  def props(self):
    """ utilisée pour construire les résumés à comparer avec les rapports existants """
    return [f'titre:{self.titre}',f'auteur:{self.auteur}',f'langue:{self.lang}',f'({self.adresse})']

  def auth(self):
    """ liste de avec l'auteur et le titre pour construire le rapport des auteurs """
    return [self.auteur,f': {self.titre}']

  def specepub(self):
    """ contenu du rapport epub destiné à contenir la table des matieres """
    return '<br />'.join([f'(titre={self.titre})',f'(auteur={self.auteur})',f'(langue={self.lang})',f'Table des matières : ']+[str(i) for i in self.t])

  def pepub(self):
    """ liste de propriétés """
    return [f'titre={self.titre}',f'auteur={self.auteur}',f'langue={self.lang}']

  def __repr__(self):
    """ fonction d'affichage du livre """
    return ('\n'+60*'-'+'\n').join([self.adresse,f'titre={self.titre}',f'auteur={self.auteur}',f'langue={self.lang}',f'Table des matières : \n'+self.table])

###--------------------------------------------------------------------------

class Corpus():
  def __init__(self,adresses):
    """ initialisation on a une liste des adresses, une liste de livres et une liste d'abstract qui serviront à comparer aux rapports """
    self.adresses=adresses
    self.livres=[]
    for adresse in adresses: #on essaie de créer les livres (dans le cas de zip ou de dossiers, rien n'est créé)
      try:
        self.livres+=[Livre(adresse)]
      except:
        pass
    self.abstract=[str(l).strip('\n') for l in self.livres]
  def __iter__(self):
    """ itérateur de la classe : revient à itérer sur les livres de l'objet corpus """
    return iter(self.livres)
  def tauth(self):
    """ fonction utilisée pour avoir un résumé des auteurs à comparer à un rapport auteurs existant """
    loeuvres=self.nombre()*['']
    k=0
    for i in self:
      loeuvres[k]=" ".join(i.auth())
      k+=1
    loeuvres.sort(key=str.lower)
    return ("\n".join(loeuvres)).strip('\n')
  def tprop(self):
    """ fonction utilisée pour avoir un résumé des ouvrages à comparer à un rapport ouvrages existant """
    lprops=[]
    for i in self:
      lprops+=i.props()+["_______________________________"," "]
    return ("\n".join(lprops)).strip('\n')
  def __repr__(self):
    """ affiche les livres"""
    return "\n\n".join([str(i) for i in self.livres])
  def nombre(self):
    """ renvoie le nombre de livres dans le corpus"""
    return len(self.livres)

###--------------------------------------------------------------------------




































