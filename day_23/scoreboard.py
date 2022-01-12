#!/usr/bin/env python3

from turtle import Turtle

FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.level = 0
        self.penup()
        self.setpos(-280, 260)
        self.write(self.level, font=FONT)
