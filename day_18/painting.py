#!/usr/bin/evn python3

from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.home()
timmy.shape('turtle')
timmy.color('cornflower blue')

colors = ['red', 'black', 'blue', 'yellow', 'pink', 'green', 'purple', 'brown', 'orange']


shape_side_nums = [n for n in range(3, 11)]

for shape in shape_side_nums:
    timmy.color(choice(colors))
    for n in range(shape):
        timmy.forward(100)
        timmy.right(360 / shape)

screen = Screen()
screen.exitonclick()

