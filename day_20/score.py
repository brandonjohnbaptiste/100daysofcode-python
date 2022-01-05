#!/usr/bin/env python3

from turtle import Turtle

FONT = ('Arial', 24, 'normal')
ALIGN = 'center'


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.sety(270)
        self.hideturtle()

    def game_over(self):
        self.sety(0)
        self.write('GAME OVER.', align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)
