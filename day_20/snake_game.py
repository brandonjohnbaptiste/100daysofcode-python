#!/usr/bin/env python3

from turtle import Turtle, Screen
from snake import Snake
from time import sleep

screen_height = 600
screen_width = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()

if __name__ == '__main__':
    game_running = True

    while game_running:
        screen.update()
        sleep(0.1)

        snake.move()







screen.exitonclick()
