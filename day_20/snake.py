#!/usr/bin/env python3

from turtle import Turtle, Screen

screen_height = 600
screen_width = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor('black')
screen.title('Snake')

screen.exitonclick()
