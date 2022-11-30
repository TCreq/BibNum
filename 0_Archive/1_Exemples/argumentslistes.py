#!/bin/env python3

### Import des modules
import sys, re

"""
    Soit L le type liste dont les elements sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.  

    Ce module contient les outils pour construire les listes a partir des arguments presentes comme enonce ci dessous

    La liste doit etre fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
    La liste peut etre fournie en argument, ou via un fichier mentionne en argument, ou bien avec rien en argument (demande)
"""

### definition des fonctions du module
def build(l0):
    """
    Cette fonction construit la liste correspondant a sa representation chaine de caractere fourni en argument.
    """
    def _build():
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1
                if i!=1:             # pour la premiere sous-liste, on ne fait rien
                    l.append(_build())    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))
                i+=1
    i = 0
    res = _build()
    return res

def listes(args=[]):
  """
  Cette fonction choisit une methode d'obtention des arguments et genere la matrice contenant la ou les listes sur
  lesquelles appliquer une fonction
  """
  if True:
    mat=[]
    if len(args)>2:                   # methode avec liste fournie en argument
      l0= args[1:]
      l=build(l0)
      mat.append(l)
    elif len(args)==2:                # methode avec liste fournie par un fichier texte
      f = open(args[1], "r")
      for line in f:
        lline = re.split(r' +',line.rstrip("\n"))
        l = build(lline)
        mat.append(l)
    else:                                 # methode avec demandes successives de listes pour l'algorithme
      print("il n'y a pas d'argument")
      l=[]
      while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
          break
        lline = re.split(r' +',line.rstrip("\n"))
        i = 0
        l=build(lline)
        mat.append(l)

    #print(f"{l=}")
    #print(f"{mat=}")
    return mat
