# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle
turtl1 = turtle.Turtle()
screen = turtle.Screen()
turtl1.speed(10)
turtle.screensize(1000000,1000000)
for i in range(1,10000000):
    turtl1.forward(i)
    turtl1.left(i)
print(screen.getshapes())

