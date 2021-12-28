#!/usr/bin/evn python3
from turtle import Turtle, Screen, colormode
from random import choice
from colorgram import extract

colormode(255)

timmy = Turtle()
timmy.speed(0)
timmy.hideturtle()

rotation = 3
amount_of_rotations = int(360 / rotation)


def random_color():
    color_objects = extract('pastel.png', 15)
    colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in color_objects]
    return choice(colors)


for n in range(amount_of_rotations):
    timmy.color(random_color())
    timmy.circle(150)
    timmy.left(rotation)

screen = Screen()
screen.exitonclick()
