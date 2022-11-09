#!/bin/env python3

### Description de la classe

""" Classe pour les cartes """

### Import des modules

import copy
import Carte as C # On évite les imports circulaires

### Definition de la classe et des fonctions de la classe

### ----------------------------------------------------------------------------

class CombinaisonImpossible(RuntimeError):
  pass

### ----------------------------------------------------------------------------

class Carre(C.Cartes):
  """ Classe de la combinaison Carré
      Un carré est un ensemble de cartes
      On le définit par rapport à une main
      A sa création, on n'enleve pas les elements de la main
      en cas d'absence de la combinaison, on remonte un erreur
  """

  def __init__(self, main):
    """ Constructeur de la classe """
    super().__init__()
    self.v=0
    valeurs=main.listv() #liste des valeurs contenues dans la main
    #print(valeurs)
    hand=main.copie() #copie de la liste des cartes
    #print([valeurs.count(i) for i in valeurs])
    for i in valeurs: #on parcourt les valeurs de la main
      if valeurs.count(i)>=4: #si la valeur est contenue 4 fois dans la main
        j=valeurs.index(i) #on recupere son index dans la liste
        self.v=hand[j].valeur #on attribue une valeur indicative au carré
        self.cartes+=[hand[j]] #on ajoute la premiere carte du carré à la liste
        for k in range(0,3): #on repete 3 fois
          j=valeurs.index(i,j+1) #a chaque fois, on regarde l'indice suivant
          self.cartes+=[hand[j]]
        break #on arrete la recherche si on a un carré
    if self.v==0 : # si on n'a pas trouvé de carré, on leve une exception
      raise CombinaisonImpossible("Pas de carré dans la main")

  def __repr__(self):
    """ Affiche le carré de façon synthétique """
    return f"carré de {self.v}"

### ----------------------------------------------------------------------------

class Brelan(C.Cartes):
  """ Classe pour les Brelans, fonctionne comme les carrés approximativement """

  def __init__(self, main):
    """ Constructeur de la classe """
    super().__init__()
    self.v=0
    valeurs=main.listv()
    #print(valeurs)
    hand=main.copie()
    #print([valeurs.count(i) for i in valeurs])
    for i in valeurs:
      if valeurs.count(i)>=3:
        j=valeurs.index(i)
        self.v=hand[j].valeur
        self.cartes+=[hand[j]]
        for k in range(0,2):
          j=valeurs.index(i,j+1)
          self.cartes+=[hand[j]]
        break
    if self.v==0 :
      raise CombinaisonImpossible("Pas de Brelan dans la main")

  def __repr__(self):
    return f"brelan de {self.v}"

### ----------------------------------------------------------------------------

class Paire(C.Cartes):
  """ Classe pour les paires, fonctionne a peu pres comme les carrés """

  def __init__(self, main):
    """ Constructeur de la classe """
    super().__init__()
    self.v=0
    valeurs=main.listv()
    #print(valeurs)
    hand=main.copie()
    #print([valeurs.count(i) for i in valeurs])
    for i in valeurs:
      if valeurs.count(i)>=2:
        j=valeurs.index(i)
        self.v=hand[j].valeur
        self.cartes+=[hand[j]]
        for k in range(0,2):
          j=valeurs.index(i,j+1)
          self.cartes+=[hand[j]]
        break
    if self.v==0 :
      raise CombinaisonImpossible("Pas de Paire dans la main")

  def __repr__(self):
    return f"Paire de {self.v}"

### ----------------------------------------------------------------------------

class Quinte(C.Cartes):
  """ Classe de la Quinte, suite de 5 cartes """

  def __init__(self,main):
    """ Constructeur de la classe """
    super().__init__()
    self.v=0
    valeurs=main.listv()
    hand=main.copie()
    for i in valeurs:
      v1=[u-1 for u in valeurs] #on construit des listes de valeurs décalées de 1 2 3 4 pour tester l'existence de cartes eligibles pour la suite
      v2=[u-2 for u in valeurs]
      v3=[u-3 for u in valeurs]
      v4=[u-4 for u in valeurs]
      if v1.count(i)>=1 and v2.count(i)>=1 and v3.count(i)>=1 and v4.count(i)>=1:
        j=valeurs.index(i)
        self.v=hand[j].valeur
        self.cartes+=[hand[j]]
        for k in range(1,5):
          j=valeurs.index(i+k)
          self.cartes+=[hand[j]]
        break
    if self.v==0:
      raise CombinaisonImpossible("Pas de Quinte dans la main")

### ----------------------------------------------------------------------------

class Quinteflush(C.Cartes):
  """ Classe de la Quinte d'une meme couleur, fonctionne similairement à la quinte """

  def __init__(self,main):
    """ Constructeur de la classe """
    super().__init__()
    self.v=0
    valeurs=main.listid()
    hand=main.copie()
    for i in valeurs:
      v1=[u-1 for u in valeurs]
      v2=[u-2 for u in valeurs]
      v3=[u-3 for u in valeurs]
      v4=[u-4 for u in valeurs]
      if v1.count(i)>=1 and v2.count(i)>=1 and v3.count(i)>=1 and v4.count(i)>=1 and hand[valeurs.index(i)].couleur==hand[valeurs.index(i+4)].couleur:
        j=valeurs.index(i)
        self.v=hand[j].valeur
        self.cartes+=[hand[j]]
        for k in range(1,5):
          j=valeurs.index(i+k)
          self.cartes+=[hand[j]]
        break
    if self.v==0:
      raise CombinaisonImpossible("Pas de Quinte Flush dans la main")

### ----------------------------------------------------------------------------






