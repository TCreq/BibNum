#!/bin/env python3

### Import des modules
import sys, re
import argumentslistes as lis

"""
    Soit L le type liste dont les elements sont soit tous de type int, soit tous de type L.
    Ce programme est appele avec le nom d'un fichier sur la ligne de commande,
    ce fichier contenant des listes de type L.
    Il sort la profondeur de chaque liste.
"""

### Creation des fonctions
def profondeur(l):
    """
    Cette fonction renvoie la profondeur de la liste passee en argument.
    """
    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)

    prof=float("-inf")
    _profondeur(l,1)
    return(prof)

### Programme principal
if __name__=="__main__":
  args=sys.argv   #recuperation des arguments
  mat=lis.listes(args)  #construction de la matrice des listes
  if mat!=[]:
    for li in mat:
      print(f"{li=}")
      print(f"{profondeur(li)=}")



