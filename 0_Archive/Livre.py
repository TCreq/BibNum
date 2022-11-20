#!/bin/env python3

### Description de la classe

""" Classe de base pour le projet librairie """

### Import des modules

import copy #Pour copier différentes listes ou objets


### Definition de la classe et des fonctions de la classe

### ----------------------------------------------------------------------------

class Erreur1(ValueError):
  """ Erreur pour ... """
  pass

### ----------------------------------------------------------------------------

class Livre():
  """ Classe des livres
  """
  table={0:"\x1b[31m",1:"\x1b[37m",2:"\x1b[31m",3:"\x1b[37m"} #table de correspondance id_couleur - couleur_affichage_carte

  def __init__(self,v=None,c=None):
    """Constructeur de la classe"""

  def __repr__(self):
    """Affiche le nom du livre?"""


#    super().__init__()


### ----------------------------------------------------------------------------

### ----------------------------------------------------------------------------

### ----------------------------------------------------------------------------
