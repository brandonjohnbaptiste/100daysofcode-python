#!/usr/bin/env python3

from turtle import Screen
from random import getrandbits
from paddle import Paddle
from ball import Ball

WIDTH = 800
HEIGHT = 600
COLOR = 'black'

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(COLOR)
screen.title('Pong!')

left_paddle = Paddle(width=20, height=100)
left_paddle.setx(-350)

right_paddle = Paddle(width=20, height=100)
right_paddle.setx(350)

ball = Ball()

screen.listen()
screen.onkeypress(left_paddle.up, 'Up')
screen.onkeypress(left_paddle.down, 'Down')

ball.setheading(45)
while True:
    ball.move()

screen.exitonclick()

