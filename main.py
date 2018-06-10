#qpy:kivy
# -*- coding: utf-8 -*-

import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Builder.load_string('''
<CarouselSlide@BoxLayout>:
    ScrollView:
        GridLayout:
            height: self.minimum_height
            do_scroll_x: False
            padding: 1
            spacing: 2
            cols:2
            size_hint: (1, 1)
            Label:
                text: 'Durée'
                size_hint: (.25, .3)
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            BoxLayout:
                size_hint: (.25, .7)
                orientation: 'vertical'
                Label:
                    id: dur
                    text: str(int(sli.value))+" mn."
                    color: (0, 1, 1, 1)
                    halign: 'center'
                    valign: 'top'
                    text_size: self.size
                Slider:
                    id: sli
                    range: (1, 20)
                    step: 1
                    value_track_width: 5
                    cursor_size: ('25sp', '25sp')
            Label:
                text: 'Objectif'
                size_hint_x: .3
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            LFontInput:
            Label:
                text: 'Moyen'
                size_hint_x: .3
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            LFontInput:
            Label:
                text: 'Consigne'
                size_hint_x: .3
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            LFontInput:
            Label:
                text: 'Observ.'
                size_hint_x: .3
                halign: 'left'
                valign: 'middle'
                text_size: self.size
            LFontInput:
                
<TpsInput@TextInput>:
    
''')

try:
    Window.softinput_mode = 'below_target'
except:
    pass

class CarouselSlide(BoxLayout):
    def build(self):
        return self


class AddButton(Button):
    def add_page(self, instance):
        instance.add_widget(CarouselSlide(allow_stretch=True))


class AikiSteps2App(App):
    ##classe pour tester kivy
    def build(self):
        pass
    pass


if __name__ == '__main__':
    AikiSteps2App().run()
