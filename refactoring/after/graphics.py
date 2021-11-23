'''
name: Jackie Himel and Erik Cohen
file: graphics.py
data: 11/15/2021
course: CS321 fall
description: simple implementation of graphics with turtle
'''

import turtle

class TurtleGraphics:
    def __init__(self):  
        self.turt = turtle.Turtle()
        self.turt.speed(0) # Speed of animation, 0 is max
    
    def turtle_style(self, shape = 'classic', color = "white", stretch_width = 1, stretch_length = 1):
        self.turt.shape(shape) # square defualt is 20,20
        self.turt.color(color)
        self.turt.shapesize(stretch_width, stretch_length) 

    def get_turtle(self):
        return self.turt

    def teleport(self, x_pos, y_pos):
        self.turt.up()
        self.turt.goto(x_pos, y_pos)
        self.turt.down()

    def make_window(self, window_title, bgcolor = "black", width = 800, height = 600):
        '''this function creates a screen object and returns it'''
        window = self.turt.getscreen() #Set the window size
        window.title(window_title)
        window.bgcolor(bgcolor)
        window.setup(width, height)
        window.tracer(0) #turns off screen updates for the window Speeds up the game
        return window
