#!/usr/bin/env python3

from turtle import Turtle

STARTING_POS = -250
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self. sety(STARTING_POS)
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)
