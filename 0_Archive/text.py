#!/bin/env python3
### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

#!/bin/env python3

from glob import glob
import sys

class Cat:
  def __init__(self,fn,show_name=False):
    self.fn = glob(fn)
    self.line = None
    self.f = None
    self.sn = show_name
    
  def __iter__(self):
    return self

  def nextFile(self):
    if self.f:        # y a-t-il un fichier ouvert ?
      # un fichier est ouvert, on le ferme car on est au bout
      self.f.close()
    if len(self.fn)==0:
      # il n'y a plus de fichier à traiter
      raise StopIteration()  # c'est la fin

    while True:  
      self.name = self.fn.pop()  # on passe au fichier suivant
      try:  
        self.f = open(self.name)
        break # fichier ouvert, mission accomplie, on sort
      except:
        # il y a problème pour l'ouvrir
        print(f"can't open {self.name} !!", file=sys.stderr)

  def __next__(self):
    while True:
      if not self.line:   # a-t-on une ligne valide ?
        # non
        self.nextFile()   # on passe au fuchier suivant

      self.line = self.f.readline()
      if self.line:
        if self.sn:
          return f"{self.name}: {self.line}"
        else:
          return self.line

c = Cat("/etc/an*",show_name=True)
for l in c:
  print(l, end="")
