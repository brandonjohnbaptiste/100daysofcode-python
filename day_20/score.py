#!/usr/bin/env python3

from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def update_score(self):
        self.score += 1

    def display_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center')
