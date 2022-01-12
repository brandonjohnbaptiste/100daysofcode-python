#!/usr/bin/env python3

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0

        self.setpos(-100, 200)
        self.write(self.p1_score, align='center', font=('Courier', 80, 'normal'))

        self.setpos(100, 200)
        self.write(self.p2_score, align='center', font=('Courier', 80, 'normal'))

    def p1_goal(self):
        self.p1_score += 1

    def p2_goal(self):
        self.p2_score += 1

    def update_scoreboard(self):
        self.clear()
        self.setpos(-100, 200)
        self.write(self.p1_score, align='center', font=('Courier', 80, 'normal'))

        self.setpos(100, 200)
        self.write(self.p2_score, align='center', font=('Courier', 80, 'normal'))