#!/usr/bin/evn python3

from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.home()
timmy.shape('turtle')
timmy.color('cornflower blue')
timmy.pensize(20)
timmy.speed(0)

colors = ['red', 'black', 'blue', 'yellow', 'pink', 'green', 'purple', 'brown', 'orange']
directions = [0, 90, 180, 270]

for n in range(100):
    timmy.color(choice(colors))
    timmy.setheading(choice(directions))
    timmy.forward(40)


screen = Screen()
screen.exitonclick()

