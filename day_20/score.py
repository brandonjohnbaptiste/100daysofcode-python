#!/usr/bin/env python3

from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.sety(270)
        self.hideturtle()

    def update_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 20, 'normal'))
