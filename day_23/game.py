#!/usr/bin/evn python3

from turtle import Screen
from time import sleep

from player import Player

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()

if __name__ == '__main__':
    print('Starting program....')

    running = True
    while running:
        screen.update()
        sleep(0.1)

screen.exitonclick()
