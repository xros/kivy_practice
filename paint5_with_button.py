#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
This is a trial from kivy's official site: 
This is the last trial on that page

Paint with clear button

http://kivy.org/docs/tutorials/firstwidget.html
Visit there for more information
"""
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from random import random

class MyPaintWidget(Widget):
    def on_touch_down(self, touch):
        color = (random(),1., 1.)
        with self.canvas:
            #"""
            #As before, we set the color for the canvas. 
            #Only this time we use the random values we generated and feed them to the color class
            #using Python’s tuple unpacking syntax "(*color)"
            #since the Color class expects three individual color components instead of just 1
            #If we were to pass the tuple directly, that would be just 1 value being passed, regardless of the fact that the tuple itself contains 3 values
            #"""
            Color(*color, mode = "hsv")                                                    #color random
            """
            Instead of creating a tuple with three random values,
            create a tuple like this: (random(), 1., 1.).
            Then, when passing it to the color instruction, 
            set the mode to HSV color space: Color(*color, mode='hsv'). 
            This way you will have a smaller number of possible colors,
            but the colors that you get will always be equally bright: only the hue changes.
            """
            d = 30.
            Ellipse(pos=(touch.x -d / 2, touch.y - d / 2), size = (d,d))    # This is a perfect circle
            # The first "d" above is for x axis, while 2nd "d" for y axis
            # Try to uncommit the line below and check the real ellipse
#            Ellipse(pos=(touch.x -d / 2, touch.y - d / 2), size = (2*d,d))
            """
             touch.ud is a Python dictionary (type <dict>) that allows us to store custom attributes for a touch
            """
            touch.ud['line'] = Line(points=(touch.x, touch.y))
            
    def on_touch_move(self, touch):
        """
            先有on_touch_down 后产成了一个touch.ud['line'] list对象，
            而后，在将任意时刻的touch.x , touch.y 累加到points点里面
            这样就画成连贯的线条了
        """
        touch.ud['line'].points += [touch.x, touch.y]       # 这个划线的程序非常科学！！！
        """一般都以这种方式,在terminal里面进行调试"""
        #print type(touch.ud['line'].points)
        print touch.ud['line']
            
            
class MyPaintApp(App):
    def build(self):
        parent = Widget()
        painter = MyPaintWidget()
        clearbtn = Button(text=u'Alex擦除', fontsize = 14)
        parent.add_widget(painter)
        parent.add_widget(clearbtn)
        
        def clear_canvas(obj):
            painter.canvas.clear()
            
        clearbtn.bind(on_release=clear_canvas)
        
        return parent
        
        
if __name__ == '__main__':
    MyPaintApp().run()
