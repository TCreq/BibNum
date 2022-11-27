#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#import copy #Pour copier différentes listes ou objets
import sys
from Livre import Livre,Corpus
from glob import glob
import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from Rapports import *

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
try:
  os.mkdir(rapports)
except:
  pass
print(f'{log=}')

###--------------------------------------------------------------------------------------

if 'init' in args:
  print('init')

if 'update' in args:
  print('update')


###-----------------------------------------------------------------
### Travail sur un corpus
###-----------------------------------------------------------------

files=glob(archive+'*')
#print(files)

c=Corpus(files)
#print(c)

Tables(c,rapports)

### Liste des Ouvrages ---------------------------------------------
# la liste des ouvrages (au format texte, PDF et epub)
# qui contient pour chaque livre son titre, son auteur,
# la langue et le nom du fichier correspondant,

Ouvrages(c,rapports)

### Liste des Auteurs
# la liste des auteurs (au format texte, PDF et epub)
# contenant pour chacun d’eux les titres de ses livres
# et le nom des fichiers associés.

Auteurs(c,rapports)

































