#!/usr/bin/evn python3

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
timmy.color('cornflower blue')

for n in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)


screen = Screen()
screen.exitonclick()

