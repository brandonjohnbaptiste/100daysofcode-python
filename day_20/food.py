#!/usr/bin/evn python3

from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        from random import randint
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.goto(x=randint(-280, 280), y=randint(-280, 280))
