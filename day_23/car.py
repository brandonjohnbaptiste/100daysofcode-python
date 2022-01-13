#!/usr/bin/env python3
from turtle import Turtle

COLOURS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


class Car(Turtle):
    def __init__(self):
        from random import choice
        super().__init__()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.shape('square')
        self.penup()
        self.color(choice(COLOURS))
        self.random_start_pos()

    def move(self, move_speed):
        self.backward(move_speed)

    def random_start_pos(self):
        from random import randint
        self.setpos(randint(280, 500), randint(-200, 290))



