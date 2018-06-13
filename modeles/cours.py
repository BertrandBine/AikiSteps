#-*- coding: utf-8 -*-
from modeles.cours_steps import Cours_Steps

class Cours:
    def __init__(self):
        self.THEMATIQUE = ''
        self.DATE = ''
        self.OBJ_GEN = ''
        self.DUREE_GEN=0 # à modifier par self.get_duree()
        self.LIEU = 'KUNHEIM'
        self.PUBLIC1 = 'Adultes'
        self.PUBLIC2 = 'Mixte'

        self.COURS_STEPS = [Cours_Steps(),]
 
    def get_duree(self):
        return sum([i.DUREE_STEP for i in self.COURS_STEPS])
    
    def add_detail(self):
        self.COURS_STEPS.append(Cours_Steps())
        