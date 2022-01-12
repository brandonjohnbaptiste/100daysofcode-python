#!/usr/bin/evn python3

from turtle import Screen
from time import sleep

from player import Player
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

if __name__ == '__main__':
    print('Starting program....')

    screen.listen()
    screen.onkeypress(player.move, 'Up')

    running = True
    while running:
        screen.update()
        sleep(0.1)

screen.exitonclick()
