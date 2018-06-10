#-*- coding: utf-8 -*-

from modeles.cours import Cours

class Gestion_Cours:
    def __init__(self):
        self.liste_cours=[]

    def load_cours(self):
        self.liste_cours.append(Cours())