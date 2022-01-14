#!/usr/bin/env python3

from turtle import Turtle

FONT = ('Arial', 24, 'normal')
ALIGN = 'center'


def grab_data():
    with open('data.txt') as data_file:
        score = data_file.read()
    return int(score)


def save_data(high_score):
    with open('data.txt', 'w') as data_file:
        data_file.write(high_score)


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = grab_data()
        self.color('white')
        self.penup()
        self.sety(270)
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            save_data(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.display_score()

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGN, font=FONT)
