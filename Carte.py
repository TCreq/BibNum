#!/bin/env python3

### Description de la classe

""" Classe pour les cartes """

### Import des modules

from random import randrange #Pour les Cartes définies aléatoirement
from random import shuffle #Pour mélanger la pioche
import copy #Pour copier différentes listes ou objets

### Definition de la classe et des fonctions de la classe

### ----------------------------------------------------------------------------

class CouleurErreur(ValueError):
  """ Erreur pour la définition de la couleur """
  pass
class DeckVide(ValueError):
  """ Erreur pour la fonction pioche """
  pass
class MainPleine(ValueError):
  """ Erreur pour le poker à 5 cartes quand on pioche avec une main pleine """
  pass

### ----------------------------------------------------------------------------

class Carte():
  """ Classe des objets Carte
      Attributs : couleur et valeur
      certaines methodes permettent d'obtenir de l'information sur la carte,
      en particulier la méthode id qui renvoie un id unique à chaque carte possible
  """
  valeurs = (list(range(7,11)) + ['Valet','Dame','Roi','As']) #liste valeurs d'origine de l'énoncé
  valeurs0 = [str(i) for i in (list(range(7,11)) + ['Valet','Dame','Roi','As'])] #liste valeurs modifiée pour contenir uniquement des str
  couleurs = ['Carreau','Pique','Coeur','Trèfle'] #liste des couleurs possibles
  cores={i:['Carreau','Pique','Coeur','Trèfle'][i] for i in range(0,4)} #table de correspondance id_couleur - couleur
  cores1={['Carreau','Pique','Coeur','Trèfle'][i]:i for i in range(0,4)} #table de correspondance couleur - id_couleur
  vals={(i+7):[str(i) for i in (list(range(7,11)) + ['Valet','Dame','Roi','As'])][i] for i in range(0,8)} #table de couleur id_valeur - valeur
  vals1={[str(i) for i in (list(range(7,11)) + ['Valet','Dame','Roi','As'])][i]:(i+7) for i in range(0,8)} #table de correspondance valeur - id_valeur
  table={0:"\x1b[31m",1:"\x1b[37m",2:"\x1b[31m",3:"\x1b[37m"} #table de correspondance id_couleur - couleur_affichage_carte

  def __init__(self,v=None,c=None):
    """Constructeur de la classe"""
    if v: #si un v est donne en argument
      if not str(v) in Carte.valeurs0: #si la valeur n'est pas admissible
        raise ValueError(f"{v}: valeur incorrecte")
      else:
        v0=Carte.vals1[str(v)] # v est un int ou str, v0 est un int
    else:
      v0 = randrange(0,len(Carte.valeurs))+7 #v0 est un int entre 7 et 14

    if c: #si c est donne en argument
      if not c in Carte.couleurs: #si la couleur n'est pas admissible
        raise CouleurErreur(f"{c}: couleur incorrecte")
      else:
        c0=Carte.cores1[c] # c est str, c0 est int entre 0 et 3
    else:
      c0 = randrange(0,len(Carte.couleurs)) # c0 est int entre 0 et 3
    self.couleur = c0 #attribut couleur int entre 0 et 3
    self.valeur = v0 #attribut valeur int entre 7 et 15

  def __repr__(self):
    """Affiche la carte avec couleur rouge si la carte est carreau ou coeur"""
    return Carte.table[self.couleur]+Carte.vals[self.valeur]+" de "+Carte.cores[self.couleur]+"\x1b[37m"

  def id(self): #fonction utile pour les hierarchies de cartes (ex: quinte flush)
    """ renvoie un id de la carte entier entre 0 et 31 """
    return 8*int(self.couleur)+int(self.valeur-7)

### --------------------------------------------------------------------------

class Cartes():
  """ Classe pour des ensembles de cartes
      Attribut principal : liste contenant des objets de type carte
      les méthodes listv et listid renvoient des listes avec les valeurs
      ou les id des cartes contenues dans la liste de l'objet
  """
  def __init__(self,c=None):
    """ Constructeur de la classe"""
    if c: # Si un objet cartes est entré en argument, on en crée une copie
      self.cartes=copy.deepcopy(c.cartes)
    else :
      self.cartes=[]

  def copie(self):
    """ renvoie une liste copiée des cartes """
    a=copy.deepcopy(self.cartes)
    return a

  def __repr__(self):
    """ affiche les cartes de la liste de cartes """
    return " , ".join([str(c) for c in self.cartes])

  def ajoute(self,c):
    """ ajoute une carte à la liste dans l'objet """
    self.cartes += [c]

  def __iadd__(self,c):
    """ Ajoute une Carte à la liste dans l'objet """
    self.cartes+=[c]
    return self

  def pioche(self):
    """ Pioche si possible une carte dans la liste des cartes (au dessus) """
    if len(self.cartes)!=0:
      return self.cartes.pop(0)
    else:
      raise DeckVide("Pas de cartes à piocher")

  def listid(self):
    """ renvoie une liste avec les id des cartes de l'objet """
    if len(self.cartes)!=0:
      return [i.id() for i in self.cartes]
    else:
      return []

  def listv(self):
    """ revoie une liste avec les valeurs des cartes de l'objet """
    if len(self.cartes)!=0:
      return [i.valeur for i in self.cartes]
    else:
      return []

  def __isub__(self,c):
    """ Retire une Carte si elle est dans le deck ou un ensemble de cartes (seulement si elles sont contenues dans le deck)"""
    if isinstance(c,Carte):
      if c.id() in self.listid():
        a=self.cartes.pop(self.listid().index(c.id()))
    elif isinstance(c,Cartes):
        for i in c.cartes:
          if isinstance(i,Carte):
            if i.id() in self.listid():
              a=self.cartes.pop(self.listid().index(i.id()))
    return self

  def melange(self):
    """ melange la liste des cartes au hasard """
    shuffle(self.cartes)

### ----------------------------------------------------------------------------

class Jeu(Cartes):
  """ Classe pour un jeu de carte : initialisé avec 32 cartes et evolue comme un ensemble quelconque de cartes """

  def __init__(self):
    """ Constructeur de la classe """
    super().__init__()
    self.cartes=32*[None]
    for i in range(0,4): # on parcours les 4 couleurs
      for j in range(0,8): # 8 cartes par couleur
        self.cartes[8*i+j]=Carte(Carte.vals[j+7],Carte.cores[i])

### ----------------------------------------------------------------------------

class Main(Cartes):
  """ Classe pour une main de joueur, peut etre complétée
      Chaque Main est liée à un jeu
  """

  def __init__(self,jeu):
    """ Constructeur de la classe """
    super().__init__()
    self.jeu=jeu

  def complete(self):
    """ Pioche une carte dans le jeu """
    try:
      self.cartes+=[self.jeu.pioche()]
    except ValueError as e:
      raise DeckVide("pus de carte pour compléter la main")

### ----------------------------------------------------------------------------





