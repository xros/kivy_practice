#!/usr/bin/env python
#-*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
# To add path for font
from kivy.resources import resource_find
from kivy.resources import resource_add_path
#from kivy.resources import resource_remove_path


resource_add_path('/home/alex/sandbox/env_27_kivy/kivy_practice/chinese_character_support/static/')
chineseFont = resource_find('DroidSansFallback.ttf')

class LoginScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        #self.cols = 3       # 3 columns 
        self.rows = 4       # 4 rows 
        self.add_widget(Label(text=u'用户名', font_name= chineseFont ))        # add widget label : content User Name
        self.username = TextInput(multiline=False, font_name= chineseFont )      # no multiline text input support
        self.add_widget(self.username)                  # add 'username' textinput
        self.add_widget(Label(text=u'密码', font_name = chineseFont))        # add widget label : content User Name
        self.password = TextInput(multiline=False, password=True)   #password auto-hidden
        self.add_widget(self.password)
        self.btn1 = Button(text=u'登录', font_name = chineseFont, font_size=14, height=30)   # add login button
        self.add_widget(self.btn1)
        self.btn2 = Button(text=u'注册', font_name = chineseFont, font_size=14) # add Sign up button
        self.add_widget(self.btn2)
        
        def on_checkbox_active(checkbox, value):            
            '''
            Once checkbox's state is changed.
            if checked, then pass "True" to on_checkbox_active
            if not, then pass "False" to on_checkbox_active
            '''
            if value:
                pass
            else:
                pass
        checkbox = CheckBox()
        checkbox.bind(active=on_checkbox_active)            #checked , then dispatch to on_checkbox_active
        self.add_widget(checkbox)                      # add check box to remember password
        self.add_widget( Label(text=u"记住密码", font_name=chineseFont) )  # add widget label as "remember password"
    
    
class MyApp(App):
    def build(self):
        return LoginScreen()
        
        
if __name__ == "__main__":
    MyApp().run()
 
