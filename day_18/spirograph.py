#!/usr/bin/evn python3
from turtle import Turtle, Screen, colormode
from random import randint

colormode(255)

timmy = Turtle()
timmy.speed('fastest')

rotation = 5
amount_of_rotations = int(360 / rotation)


def random_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


for n in range(amount_of_rotations):
    timmy.color(random_color())
    timmy.circle(150)
    timmy.left(rotation)

screen = Screen()
screen.exitonclick()
