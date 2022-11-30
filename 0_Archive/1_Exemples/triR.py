#!/bin/env python3

### Import des modules
import sys, re
import argumentslistes as lis

"""
    Soit L le type liste dont les elements sont soit tous de type int, soit tous de type L.

    Ce programme lit des liste de type L sur l'entree standard, au format
    [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
    et sort cette liste dans laquelle les sous-listes d'entiers sont triees.  
"""

### Creation des fonctions
def tri(l):
    """
    Cette fonction recursive tri la liste passee en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

### Programme principal
if __name__=="__main__":
    args=sys.argv
    mat=lis.listes(args)
    if mat!=[]:
      for li in mat:
        tri(li)
        print(f"{li=}")
