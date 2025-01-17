#!/usr/bin/env python
#-*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        #self.cols = 3       # 3 columns 
        self.rows = 1       # 4 rows 
        self.username = TextInput(text="boy inside", multiline=False, focus = True )      # no multiline text input support
        
        #def on_enter(instance, value):
        #    print ('User pressed enter in', instance)
        #self.username.bind(on_text_validate=on_enter)
        #self.username(focus=True)
        self.add_widget(self.username)                  # add 'username' textinput
        
        
    
class MyApp(App):
    def build(self):
        return LoginScreen()
        
        
if __name__ == "__main__":
    MyApp().run()