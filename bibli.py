#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#import copy #Pour copier différentes listes ou objets
import sys
from Livre import Livre

### -------------------------------------------------------------------------------------------
### Recuperation des arguments ###

args=sys.argv
#print(args)

### ---------------------------------------------------------------------------------------------
### Configuration des Repertoires de lecture, ecriture, log ###

config='bibli.conf'

if '-c' in args:
  config=args[args.index('-c')+1]
  print(f'{config=}')

archive=''
rapports=''
log=''

il = 0
with open(config,"r") as f:
  for line in f:
    il += 1
    print(f"{il:03d}: {line}", end="")
    if il==1:
      archive=line.strip()
    elif il==2:
      rapports=line.strip()
    elif il==3:
      log=line.strip()

print(f'{archive=}')
print(f'{rapports=}')
print(f'{log=}')

###--------------------------------------------------------------------------------------

if 'init' in args:
  print('init')

if 'update' in args:
  print('update')


















































