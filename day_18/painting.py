#!/usr/bin/evn python3
import turtle
from turtle import Turtle, Screen
from random import choice, randint

turtle.colormode(255)

timmy = Turtle()
timmy.home()
timmy.shape('turtle')
timmy.color('cornflower blue')
timmy.pensize(20)
timmy.speed(0)

directions = [0, 90, 180, 270]

for n in range(200):
    rand_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    timmy.color(rand_color)
    timmy.setheading(choice(directions))
    timmy.forward(30)


screen = Screen()
screen.exitonclick()

