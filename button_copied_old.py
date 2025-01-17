from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        #self.cols = 3       # 3 columns 
        self.rows = 3       # 3 rows 
        self.add_widget(Label(text='User Name'))        #add widget label : content User Name
        self.username = TextInput(multiline=False)      # no multiline text input support
        self.add_widget(self.username)                  #add 'username' textinput
        self.add_widget(Label(text='Pass Word'))        #add widget label : content User Name
        self.password = TextInput(multiline=False, password=True)   #password auto-hidden
        self.add_widget(self.password)
        self.btn1 = Button(text='Login', fontsize=14)   #add a button
        self.add_widget(self.btn1)
        """
    Add callback to the button if it's pressed
        """
        self.btn1.bind(on_press=buttonCallback)
    
    def buttonCallback(instance):
        print "The button is %s is being pressed" % instance.text
    
        
    
        
        
class MyApp(App):
    def build(self):
        return LoginScreen()
        
        
if __name__ == "__main__":
    MyApp().run()
