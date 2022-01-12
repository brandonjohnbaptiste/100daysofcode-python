#!/usr/bin/env python3

from turtle import Turtle

FONT = ('Courier', 25, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.level = 1
        self.penup()
        self.setpos(-285, 250)
        self.write(f'Level: {self.level}', font=FONT)
