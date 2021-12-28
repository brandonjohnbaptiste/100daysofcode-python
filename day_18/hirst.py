#!/usr/bin/env python3

from colorgram import extract
from turtle import Turtle, Screen, colormode
from random import choice

colors_objects = extract('pastel.png', 16)
colors = [(color.rgb.r, color.rgb.b, color.rgb.b) for color in colors_objects]
dot_size = 20
colormode(255)

initial_x = -250
initial_y = -200

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.setposition(initial_x, initial_y)

for y in range(10):
    turtle.sety(initial_y + (y * 50))
    turtle.setx(initial_x)
    for x in range(10):
        turtle.pendown()
        turtle.dot(dot_size, choice(colors))
        turtle.penup()
        turtle.setx(turtle.xcor() + 50)


screen = Screen()
screen.exitonclick()
