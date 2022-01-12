#!/usr/bin/env python3

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
COLOR = 'black'

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor(COLOR)
screen.title('Pong!')
screen.tracer(0)

left_paddle = Paddle(width=20, height=100)
left_paddle.setx(-350)

right_paddle = Paddle(width=20, height=100)
right_paddle.setx(350)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(left_paddle.up, 'Up')
screen.onkeypress(left_paddle.down, 'Down')

screen.onkeypress(right_paddle.up, 'w')
screen.onkeypress(right_paddle.down, 's')

ball.setheading(-115)

while True:
    screen.update()

    if ball.distance(left_paddle) < 40 or ball.distance(right_paddle) < 40 and abs(ball.xcor()) > 320:
        ball.bounce()
        ball.travelling *= -1

    if ball.xcor() > 380:
        scoreboard.p1_goal()
        scoreboard.update_scoreboard()
        ball.travelling *= -1
        ball.reset()
    elif ball.xcor() < -380:
        scoreboard.p2_goal()
        scoreboard.update_scoreboard()
        ball.travelling *= -1
        ball.reset()

    if abs(ball.ycor()) > 280:
        ball.bounce()

    ball.move()




screen.exitonclick()

