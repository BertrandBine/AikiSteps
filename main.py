#qpy:kivy
#-*- coding: utf-8 -*-


import kivy
kivy.require('1.10.0')
from kivy.app import App
from controleurs.gestion_cours import Gestion_Cours
from vues.detail_cours_view import Detail_Cours_View

class AikiSteps2App(App):
    ##classe pour tester kivy
    def build(self):
        self.gestion_cours=Gestion_Cours()
        self.DCV=Detail_Cours_View()
        return self.DCV
        
if __name__ == '__main__': 
    AikiSteps2App().run()