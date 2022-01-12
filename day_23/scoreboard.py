#!/usr/bin/env python3

from turtle import Turtle

FONT = ('Courier', 25, 'normal')
INITIAL_X = -285
INITIAL_Y = 250


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.level = 1
        self.penup()
        self.setpos(INITIAL_X, INITIAL_Y)
        self.write(f'Level: {self.level}', font=FONT)

    def refresh_display(self):
        self.clear()
        self.setpos(INITIAL_X, INITIAL_Y)
        self.write(f'Level: {self.level}', font=FONT)

    def next_level(self):
        self.level += 1
        self.refresh_display()
