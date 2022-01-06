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

if getrandbits(1):
    ball.travelling = 'left'
else:
    ball.travelling = 'right'

while True:
    if ball.travelling == 'left':
        ball.forward(5)
    else:
        ball.backward(5)

    if ball.distance(right_paddle) < 25:
        print('hit right paddle')
        ball.rebound()
    elif ball.distance(left_paddle) < 25:
        print('hit left paddle')
        ball.rebound()


screen.exitonclick()

