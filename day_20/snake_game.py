#!/usr/bin/env python3

from turtle import Screen
from snake import Snake
from time import sleep

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

if __name__ == '__main__':
    game_running = True

    while game_running:
        screen.update()
        sleep(0.1)

        snake.move()


    screen.exitonclick()
