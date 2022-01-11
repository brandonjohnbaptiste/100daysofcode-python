#!/usr/bin/env python3

from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.travelling = -1

    def move(self):
        if self.travelling == -1:
            self.forward(3)
        elif self.travelling == 1:
            self.backward(3)

    def move_right(self):
        self.setheading(self.heading() + 20)

    def bounce(self):
        new_heading = self.heading() * -1
        self.setheading(new_heading)
