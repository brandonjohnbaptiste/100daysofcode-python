#!/usr/bin/env python3

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.travelling = 'left'

    def move(self):
        self.forward(5)

    def move_right(self):
        self.setheading(self.heading() + 20)

    def rebound(self):
        if self.travelling == 'left':
            self.travelling = 'right'
        else:
            self.travelling = 'left'
