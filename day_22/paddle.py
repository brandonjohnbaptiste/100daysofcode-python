#!/usr/bin/env python3

from turtle import Turtle

PADDLE_COLOR = 'white'
TURTLE_SIZE_DEFAULT = 20


class Paddle(Turtle):
    def __init__(self, height, width):
        super().__init__()
        self.turtlesize(stretch_wid=height / TURTLE_SIZE_DEFAULT, stretch_len=width / TURTLE_SIZE_DEFAULT)
        self.color(PADDLE_COLOR)
        self.shape('square')
        self.penup()

