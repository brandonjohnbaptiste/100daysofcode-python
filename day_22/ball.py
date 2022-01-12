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
        self.speed = 3

    def move(self):
        if self.travelling == -1:
            self.forward(self.speed)
        elif self.travelling == 1:
            self.backward(self.speed)

    def move_right(self):
        self.setheading(self.heading() + 20)

    def bounce(self):
        new_heading = self.heading() * -1
        self.speed = self.speed * 1.05
        self.setheading(new_heading)

    def random_heading(self):
        from random import choice
        headings = [45, 135, 225]
        self.setheading(choice(headings))

    def reset(self):
        self.random_heading()
        self.speed = 3
        self.goto(0, 0)
