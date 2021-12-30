#!/usr/bin/env python3

from turtle import Turtle, Screen

screen_height = 600
screen_width = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor('black')
screen.title('Snake')


def create_turtle():
    t = Turtle(shape='square')
    t.color('white')
    return t


turtles = [create_turtle() for i in range(3)]
init_x = 0
init_y = 0
offset = 20

for turtle in turtles:
    turtle.setpos(x=(init_x - (offset * turtles.index(turtle))), y=init_y)

screen.exitonclick()
