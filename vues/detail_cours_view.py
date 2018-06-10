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

Builder.load_file('./vues/detail_cours_view.kv')

Builder.load_string('''
<CarouselSlide@BoxLayout>:
    id:SV
    allow_stretch: True
    ScrollView:
        id: sv
        GridLayout:
            height: max(self.minimum_height, sv.height)
            do_scroll_x: False
            padding: 1
            spacing: 1
            cols:2
            size_hint: (1, None)
            Label:
                text: 'Durée'
                size_hint: (.2, .3)
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            BoxLayout:
                size_hint: (.2, .6)
                orientation: 'vertical'
                Label:
                    id: DUREE_STEP
                    thefield: "DUREE_STEP"
                    text: str(int(sli.value)) + " mn."
                    color: (0, 1, 1, 1)
                    halign: 'center'
                    valign: 'top'
                    text_size: self.size
                Slider:
                    id: sli
                    range: (0, 20)
                    step: 1
                    value_track_width: 5
                    cursor_size: ('25sp', '25sp')
                    sensitivity: 'handle'
                    on_touch_up: app.get_tps(sli)
            Label:
                text: 'Objectif'
                size_hint_x: .3
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            LFontInput:
                thefield: "OBJ_STEP"
            Label:
                text: 'Moyen'
                size_hint_x: .3
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            LFontInput:
                thefield: "MOYEN"
            Label:
                text: 'Consigne'
                size_hint_x: .3
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            LFontInput:
                thefield: "CONSIGNE"
            Label:
                text: 'Observ.'
                size_hint_x: .3
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            LFontInput:
                thefield: "OBSERV"

<DurTot@Label>:
    color: (1, 1 , 1, 1)
    color: (0, 1, 1, 1)
    font_size: '18sp'
    halign: 'left'
    valign: 'middle'
    text_size: self.size

<LFontInput@TextInput>:
    font_size: '16sp'
    write_tab: False
    input_type: 'text'
    multiline: True
    focus: True
    size_hint_y: .2
''')

try:
    Window.softinput_mode = 'below_target'
except:
    pass

class CarouselSlide(BoxLayout):
    def build(self):
        return self

class LFontInput(TextInput):
    def build(self):
        return self

    def next_widget(self):
        self.get_focus_next().focus = True

class DurTot(Label):
    def build(self):
        return self

class AddButton(Button):
    def add_page(self, instance):
        instance.add_widget(CarouselSlide(allow_stretch=True))
        instance.load_next()

class DelButton(Button):
    pass

class Detail_Cours_View(Screen):
    ##classe pour tester kivy
    def __init__(self, **kwargs):
        super(Detail_Cours_View, self).__init__(**kwargs)

    def build(self):
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

    def get_car(self, thecar=0):
        i=[i for i in self.root.walk() if type(i) == Carousel]
        return i[thecar]

    def get_tps(self, *args):
        self.get_car(0)
        tot=[]
        wids=[]
        theslides=self.get_car(1).slides[:]
        for i in theslides:
            for j in i.walk():
                try:
                    if type(j) == Slider and not j in wids:
                        tot.append(j.value)
                        wids.append(j)
                except:
                    pass
        [i for i in self.get_car(0).walk()][11].text = str(int(sum(tot))) + " mn."
        
    def summerize(self):
        ET=self.entete()
        DE=self.detail()
        result=''
        dbrow=[]
        RUB_ET=['Thematique', \
                'Date', \
                'Objectif cours', \
                'Duree', \
                'Lieu', \
                'Public1', \
                'Public2']
        for i in ET:
            dbrow.append(i)
            theindex=ET.index(i)
            try:
                print i[0].thefield
            except:
                pass
            if RUB_ET[theindex] != 'Public2':
                titre=RUB_ET[theindex]
                if titre == 'Public1': titre = 'Public'
                result += titre + ' : ' + i[1] +'\n'
            else:
                try:
                    result = result[:-2] + ' (' + i[1] + ')\n'
                except:
                    pass
        result += '=='*10 + '\n'
        for i in DE[1:-1]:
            dbrow.append(i)
            if 'mn.' in i[1]: result += '\n'
            result += capitalize(i[0].thefield)+ ": " + i[1] + '\n'
        
        if self.db != None:
            for i in dbrow:
                print i[0].thefield," : ", i[1]
        
        return result

    def get_texts(self,the_slides):
        result=[]
        wids=[]
        for i in the_slides:
            for j in i.walk():
                try:
                    if (j not in wids) and ((type(j) not in [Label, Button, ToggleButton, AddButton, DelButton]) or (type(j) == ToggleButton and j.state == 'down') or (' mn.' in j.text)):
                        result.append((j, j.text))
                        wids.append(j)
                except:
                    pass
        return result

    def entete(self):
        return self.get_texts(self.get_car(0).slides[0:1])[:]

    def detail(self):
        return self.get_texts(self.get_car(1).slides[:])[:]

    def select_text(self, instance):
        instance.select_text(0, len(instance.text))
        instance.cut()
        instance.delete_selection()
        instance.text = ''
        