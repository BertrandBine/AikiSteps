#qpy:kivy
#-*- coding: utf-8 -*-

import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window

import os
import sqlite3 as sq
from string import capitalize
from modeles.cours_steps import Cours_Steps

try:
    Window.softinput_mode = 'below_target'
except:
    pass

Builder.load_file('./vues/detail_cours_view.kv')

class CarouselSlide(BoxLayout):
    def build(self):
        return self

    def get_le_cours_details(self, instance):
        return self.root.get_cours_data.COURS_STEP[self.index]

class LFontInput(TextInput):
    def build(self):
        return self

    def next_widget(self):
        self.get_focus_next().focus = True

class DurTot(Label):
    def build(self):
        return self

class RightButton(Button):
    def build(self):
        return self
    
class AddButton(Button):
    def add_page(self, instance):
        CS=Cours_Steps()
        instance.details.append(CS)
        instance.add_widget(CarouselSlide(allow_stretch=True, details=CS))
        instance.load_slide(instance.slides[-1])
    pass

class DelButton(Button):
    def build(self):
        return self

class Detail_Cours_View(Screen):
    ##vue principale kivy
    def __init__(self, **kwargs):
        super(Detail_Cours_View, self).__init__(**kwargs)
    
    def build(self):
        self.duration=0
        global sq
        try:
            self.db=sq.connect("AIKIDB")
            self.fields = ['THEME', \
                          'DATE', \
                          'OBJ_GEN', \
                          'DUREE_GEN', \
                          'LIEU', \
                          'PUBLIC1', \
                          'PUBLIC2', \
                          'DUREE_STEP', \
                          'OBJ_STEP', \
                          'MOYEN_STEP', \
                          'CONSIGNE', \
                          'OBSERV']
        except:
            print "Pas de base disponible"
            self.db = None
            self.fields = None
        self.prepare()

    # def get_car(self, thecar=0):
    #     #recherche le Carousel 0
    #     i=[i for i in self.root.walk() if type(i) == Carousel]
    #     return i[thecar]

    # def summerize(self):
    #     #résume le cours en un texte
    #     ET=self.entete()
    #     DE=self.detail()
    #     result=''
    #     dbrow=[]
    #     RUB_ET=['Thematique', \
    #             'Date', \
    #             'Objectif cours', \
    #             'Duree', \
    #             'Lieu', \
    #             'Public1', \
    #             'Public2']
    #     for i in ET:
    #         dbrow.append(i)
    #         theindex=ET.index(i)
    #         try:
    #             print i[0].thefield
    #         except:
    #             pass
    #         if RUB_ET[theindex] != 'Public2':
    #             titre=RUB_ET[theindex]
    #             if titre == 'Public1': titre = 'Public'
    #             result += titre + ' : ' + i[1] +'\n'
    #         else:
    #             try:
    #                 result = result[:-2] + ' (' + i[1] + ')\n'
    #             except:
    #                 pass
    #     result += '=='*10 + '\n'
    #     for i in DE[1:-1]:
    #         dbrow.append(i)
    #         if 'mn.' in i[1]: result += '\n'
    #         result += capitalize(i[0].thefield)+ ": " + i[1] + '\n'
        
    #     if self.db != None:
    #         for i in dbrow:
    #             print i[0].thefield," : ", i[1]
        
    #     return result

    # def get_texts(self,the_slides):
    #     #récupère les textes des slides
    #     result=[]
    #     wids=[]
    #     for i in the_slides:
    #         for j in i.walk():
    #             try:
    #                 if (j not in wids) and ((type(j) not in [Label, Button, ToggleButton, AddButton, DelButton]) or (type(j) == ToggleButton and j.state == 'down') or (' mn.' in j.text)):
    #                     result.append((j, j.text))
    #                     wids.append(j)
    #             except:
    #                 pass
    #     return result

    # def entete(self):
    #     #récupère l'en-tête du cours
    #     return self.get_texts(self.get_car(0).slides[0:1])[:]

    # def detail(self):
    #     #récupère le détail du cours
    #     return self.get_texts(self.get_car(1).slides[:])[:]

    # def select_text(self, instance):
    #     #selection le texte et le supprime
    #     instance.select_text(0, len(instance.text))
    #     instance.cut()
    #     instance.delete_selection()
    #     instance.text = ''
    
    def get_cours_data(self):
        #charge le cours
        self.app=App.get_running_app()
        self.app.gestion_cours.load_cours()
        le_cours=self.app.gestion_cours.liste_cours[0]
        return le_cours