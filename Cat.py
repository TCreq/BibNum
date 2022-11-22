#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#import copy #Pour copier différentes listes ou objets
import sys

from glob import glob
import sys

class Cat:
  def __init__(self,fn,show_name=False):
    self.fn = glob(fn)
    self.sn = show_name
    self.files = []      # va contenir des tuples (nom_fichier,fichier)
    for fn in list(self.fn): # on essaie d'ouvrir tous les fichiers
      try:
        f = open(self.fn.pop(0))
        self.files.append((fn,f))  # succès, on mémorise ce tuple
      except :
        print(f"can't open {fn} !", file=sys.stderr)  # échec, donc non mémorisé
    # ici, on a dans files tous les fichiers ouverts
    self.iter = iter(self.files)   # pour itérer sur la liste des couples
    self.curfile = next(self.iter) # le couple courant
    #print("fichier courant",self.curfile)
    if not self.sn:
      print(f"{self.curfile[0]}:") # un message de suivi

  def __iter__(self):
    return self

  def _formate_line(self,line):
    """ renvoie la ligne éventuellement précédée du nom de fichier la contenant """
    if self.sn:
      return f"{self.curfile[0]}: {line}"
    else:
      return line

  def __next__(self):
    filename = self.curfile[0]  # nom du fichier courant
    file = self.curfile[1]      # fichier courant
    line = file.readline()      # ligne suivante
    if line:      # il y a bien une ligne
      return self._formate_line(line) # on la renvoie
    else:      # ici, on n'a pas récupéré de ligne   
      file.close()          # on ferme le fichier courant, car on est au bout
      self.curfile = next(self.iter)   # on passe au fichier suivant

      if not self.sn:
        print(f"{self.curfile[0]}:")  # un message de suivi

      filename = self.curfile[0]
      file = self.curfile[1]

      line = file.readline()
      return self._formate_line(line)



c = Cat("sample/*")
for line in c:
  print(line, end="")















































