#!/bin/env python3

### Import des modules
import sys, re
import argumentslistes as lis

"""
    Soit L le type liste dont les elements sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.

    Ce programme est appele avec une liste de type L sur la ligne de commande, ou un fichier contenant la liste, ou alors
    aucun argument (Cf. Module argumentslistes)

    et sort le min des max de ses sous-listes.  

    Avec la liste l ci-dessus, la liste des max est [2, 4, 5, 3, 2, 9] donc le programme sort 2.

    La liste doit etre fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
"""

### Creation des Fonctions
def minmax(l):
    """
    Cette fonction recursive retourne le minmax de la liste passÃ©e en argument.
    """
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

### Programme principal
if __name__=="__main__":
  args=sys.argv
  mat=lis.listes(args)
  if mat!=[]:
    for li in mat:
      maxi = []
      minmax(li)
      print("le minimum des maximums pour ",li," est: ",min(maxi))

