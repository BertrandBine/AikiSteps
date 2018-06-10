#-*- coding: utf-8 -*-

class Cours:
    def __init__(self):
        self.THEMATIQUE = ''
        self.DATE = ''
        self.OBJ_GEN = ''
        self.LIEU = ''
        self.PUBLIC1 = ''
        self.PUBLIC2 = ''

        self.COURS_STEPS = []
 
    def get_duree(self):
        return sum([i.DUREE_STEP for i in self.COURS_STEPS])
    