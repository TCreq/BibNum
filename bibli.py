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
import logging

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


#Setup du fichier log
logging.basicConfig(filename=log, level=logging.INFO, format="[%(levelname)s][%(asctime)s] %(message)s")

#print(f'{archive=}')
#print(f'{rapports=}')
try:
  os.mkdir(rapports)
  logging.info(f"Creation de répertoire "+rapports)
except:
  pass
#print(f'{log=}')

###--------------------------------------------------------------------------------------

def init(archive,rapports):
  #print('init')
  files=glob(archive+'*')
  #print(files)
  c=Corpus(files)
  #print(c)
  Ouvrages(c,rapports)
  Auteurs(c,rapports)
  Tables(c,rapports)

if 'init' in args:
  init(archive,rapports)

def update(archive,rapports):
  #print('update')
  files=glob(archive+'*')
  #print(files)
  c=Corpus(files)
  #print(c)
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
      #print("absence")
      os.remove(corres[i])
      logging.info(f"Suppression de "+corres[i])
      for r in glob(corres[i][:-3]+'*'):
        try:
          os.remove(r)
          logging.info(f"Suppression de "+r)
        except:
          pass
  k=10
  for l in c:
    if not (l.abstract in rapps):
      #print("difference")
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
      #print("difference ouvrages")
      os.remove(rapports+"ouvrages.txt")
      logging.info(f"Suppression de "+rapports+"ouvrages.txt")
      os.remove(rapports+"ouvrages.pdf")
      logging.info(f"Suppression de "+rapports+"ouvrages.pdf")
      os.remove(rapports+"ouvrages.epub")
      logging.info(f"Suppression de "+rapports+"ouvrages.epub")
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
      #print("difference auteurs")
      os.remove(rapports+"auteurs.txt")
      logging.info(f"Suppression de "+rapports+"auteurs.txt")
      os.remove(rapports+"auteurs.pdf")
      logging.info(f"Suppression de "+rapports+"auteurs.pdf")
      os.remove(rapports+"auteurs.epub")
      logging.info(f"Suppression de "+rapports+"auteurs.epub")
    except:
      pass
    Auteurs(c,rapports)

if 'update' in args:
  update(archive,rapports)















