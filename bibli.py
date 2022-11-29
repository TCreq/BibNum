#!/bin/env python3
### Description de la classe

""" Programme Principal """

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

#print(f'{archive=}')
#print(f'{rapports=}')
try:
  os.mkdir(rapports)
except:
  pass
#print(f'{log=}')

###--------------------------------------------------------------------------------------

if 'init' in args:
  print('init')
  ###-----------------------------------------------------------------
  ### Travail sur un corpus
  ###-----------------------------------------------------------------
  files=glob(archive+'*')
  #print(files)
  c=Corpus(files)
  #print(c)
  ### Liste des Ouvrages ---------------------------------------------
  # la liste des ouvrages (au format texte, PDF et epub)
  # qui contient pour chaque livre son titre, son auteur,
  # la langue et le nom du fichier correspondant,
  Ouvrages(c,rapports)
  ### Liste des Auteurs ----------------------------------------------
  # la liste des auteurs (au format texte, PDF et epub)
  # contenant pour chacun d’eux les titres de ses livres
  # et le nom des fichiers associés.
  Auteurs(c,rapports)
  ### Tables des Matieres --------------------------------------------
  # plus 3 documents par livre (une version texte, PDF et epub),
  # contenant sa table des matières.
  Tables(c,rapports)


if 'update' in args:
  print('update')
  ###-----------------------------------------------------------------
  ### Travail sur un corpus
  ###-----------------------------------------------------------------
  files=glob(archive+'*')
  #print(files)
  c=Corpus(files)
  #print(c)
  ### Travail sur les Deltas
  files=glob(rapports+'*'+'r.txt')
  fouv=rapports+"ouvrages.txt"
  faut=rapports+"auteurs.txt"
  #print(files)
  rapps=[]
  corres=dict({})
  for i in files:
    il = 0
    txt=''
    with open(i,"r") as f:
      for line in f:
        txt+=line
        il+=1
    rapps+=[txt.strip('\n')]
    corres[txt.strip('\n')]=i
  #print("abst",c.abstract)
  #print("rapps",rapps)
  for i in rapps:
    if not (i in c.abstract):
      os.remove(corres[i])
  k=10
  for l in c:
    if not (l.abstract in rapps):
      RTXT(l,rapports,k)
      RPDF(l,rapports,k)
      REPUB(l,rapports,k)
      k+=1
  try:
    txt=''
    with open(fouv,"r") as f:
      for line in f:
        txt+=line
    rouv=txt.strip('\n')
  except:
    rouv=''
  #print("\ntest1\n\n",c.tprop(),rouv)
  #print("\n\nresultat",c.tprop()==rouv)
  if not (c.tprop()==rouv):
    try:
      os.remove(rapports+"ouvrages.txt")
      os.remove(rapports+"ouvrages.pdf")
      os.remove(rapports+"ouvrages.epub")
    except:
      pass
    Ouvrages(c,rapports)
  try:
    txt=''
    with open(faut,"r") as f:
      for line in f:
        txt+=line
    raut=txt.strip('\n')
  except:
    raut=''
  #print("\ntest2\n\n",c.tauth(),raut)
  #print("\n\nresultat",c.tauth()==raut)
  if not (c.tauth()==raut):
    try:
      os.remove(rapports+"auteurs.txt")
      os.remove(rapports+"auteurs.pdf")
      os.remove(rapports+"auteurs.epub")
    except:
      pass
    Auteurs(c,rapports)


### Travail sur le log

#with open(log,"w") as f:
#  for l in c:
#    print('a',file=f) # ici il me faut une fonction sur le livre pour identifier le livre














