"""
This is a trial from kivy's official site: 
http://kivy.org/docs/tutorials/firstwidget.html
Visit there for more information
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(1,1,0)
            d = 30.
            Ellipse(pos=(touch.x -d / 2, touch.y - d / 2), size = (d,d))    # This is a perfect circle
            # The first "d" above is for x axis, while 2nd "d" for y axis
            # Try to uncommit the line below and check the real ellipse
#            Ellipse(pos=(touch.x -d / 2, touch.y - d / 2), size = (2*d,d))
            
            
class MyPaintApp(App):
    def build(self):
        return MyPaintWidget()
        
        
if __name__ == '__main__':
    MyPaintApp().run()