#!/bin/env python3
### Description de la classe

""" Programme Principal """

### Import des modules

#import copy #Pour copier différentes listes ou objets
import sys
from Livre import Livre,Corpus
from glob import glob
import os
from Rapports import *
import logging

### -------------------------------------------------------------------------------------------
### Recuperation des arguments ###

args=sys.argv

### ---------------------------------------------------------------------------------------------
### Configuration des Repertoires de lecture, ecriture, log ###

config='bibli.conf' #par défaut, le fichier conf est dans le répertoire courant avec ce nom

# exemple d'entrée : ./bibli.py -c bibli2.conf update
if '-c' in args:
  config=args[args.index('-c')+1]
  #print(f'{config=}')

archive=''
rapports=''
log=''

il = 0
with open(config,"r") as f: #on ouvre le fichier de config
  for line in f:
    il += 1
    #print(f"{il:03d}: {line}", end="")
    if il==1:
      archive=line.strip() #repertoire de l'archive
      if archive[-1]!="/":
        archive+="/" #on ajoute le /
    elif il==2:
      rapports=line.strip() #repertoire des rapports
    elif il==3:
      log=line.strip() #adresse du fichier log


#Setup du fichier log
logging.basicConfig(filename=log, level=logging.INFO, format="[%(levelname)s][%(asctime)s] %(message)s")

#print(f'{archive=}')
#print(f'{rapports=}')
try:
  os.mkdir(rapports)  #on essaie de créer le répertoire de rapports
  logging.info(f"Creation de répertoire "+rapports)
except:
  pass
#print(f'{log=}')

###--------------------------------------------------------------------------------------

def init(archive,rapports): #programme quand on a la commande init
  #print('init')
  files=glob(archive+'*') #recupere tous les fichiers de l'archive
  #print(files)
  c=Corpus(files) #création du groupe de livres
  #print(c)
  Ouvrages(c,rapports) #creation du rapport sur les ouvrages (3 versions)
  Auteurs(c,rapports) #creation du rapport des auteurs (3 versions)
  Tables(c,rapports) #creation des rapports des tables des matieres (3 par livre)

if 'init' in args:
  init(archive,rapports)

def update(archive,rapports): #programme quand on a la commande update
  #print('update')
  files=glob(archive+'*') #recupere tous les fichiers de l'archive
  #print(files)
  c=Corpus(files) #création du groupe de livres
  #print(c)
  files=glob(rapports+'*'+'r.txt') #recupere tous les rapports des tables des matieres de l'archive au format txt
  fouv=rapports+"ouvrages.txt" #recupere l'adresse du rapport d'ouvrages au format txt
  faut=rapports+"auteurs.txt" #recupere l'adresse du rapport d'auteurs au format txt
  #print(files)
  rapps=[] #on dresse une liste des rapports
  corres=dict({}) #dictionnaire destiné à faire correspondre au texte d'un rapport son adresse
  for i in files: #on parcourt les fichiers
    txt='' #texte vide
    with open(i,"r") as f:
      for line in f: #on parcours les lignes du fichier
        txt+=line #on ajoute la ligne au texte
    rapps+=[txt.strip('\n')] #le rapport simplifié sans les sauts de lignes
    corres[txt.strip('\n')]=i #l'adresse du rapport
  #print("abst",c.abstract)
  #print("rapps",rapps)
  for i in rapps: #on parcourt les rapports simplifiés
    if not (i in c.abstract): #si le rapport simplifié n'est pas dans les rapports simplifiés de l'archive actuelle
      #print("absence")
      os.remove(corres[i]) #on supprime le rapport
      logging.info(f"Suppression de "+corres[i])
      for r in glob(corres[i][:-3]+'*'): #on supprime les autres rapports correspondants
        try:
          os.remove(r)
          logging.info(f"Suppression de "+r)
        except:
          pass
  k=10
  for l in c: #on parcourt l'archive actuelle
    if not (l.abstract in rapps): #si le rapport pour le livre actuel n'est pas déjà dans les rapports existantes
      #print("difference")
      RTXT(l,rapports,"U_"+str(k)) #on génere tous les rapports
      RPDF(l,rapports,"U_"+str(k))
      REPUB(l,rapports,"U_"+str(k))
      k+=1
  try:
    txt=''
    with open(fouv,"r") as f: #on essaie constituer le rapport simplifié des ouvrages
      for line in f:
        txt+=line
    rouv=txt.strip('\n')
  except:
    rouv='' #en cas d'absence, texte vide
  #print("\ntest1\n\n",c.tprop(),rouv)
  #print("\n\nresultat",c.tprop()==rouv)
  if not (c.tprop()==rouv): #si les ouvrages actuels ne correspondent pas au rapport existant
    try:
      #print("difference ouvrages")
      os.remove(rapports+"ouvrages.txt")
      logging.info(f"Suppression de "+rapports+"ouvrages.txt") #on supprime tous les rapports sur les ouvrages
      os.remove(rapports+"ouvrages.pdf")
      logging.info(f"Suppression de "+rapports+"ouvrages.pdf")
      os.remove(rapports+"ouvrages.epub")
      logging.info(f"Suppression de "+rapports+"ouvrages.epub")
    except:
      pass
    Ouvrages(c,rapports)
  try:
    txt=''
    with open(faut,"r") as f: #on essaie constituer le rapport simplifié des auteurs
      for line in f:
        txt+=line
    raut=txt.strip('\n')
  except:
    raut=''
  #print("\ntest2\n\n",c.tauth(),raut)
  #print("\n\nresultat",c.tauth()==raut)
  if not (c.tauth()==raut): #si les auteurs actuels ne correspondent pas au rapport existant
    try:
      #print("difference auteurs")
      os.remove(rapports+"auteurs.txt")
      logging.info(f"Suppression de "+rapports+"auteurs.txt") #on supprime les rapports sur les auteurs
      os.remove(rapports+"auteurs.pdf")
      logging.info(f"Suppression de "+rapports+"auteurs.pdf")
      os.remove(rapports+"auteurs.epub")
      logging.info(f"Suppression de "+rapports+"auteurs.epub")
    except:
      pass
    Auteurs(c,rapports)

if 'update' in args:
  update(archive,rapports)


print("fin")












