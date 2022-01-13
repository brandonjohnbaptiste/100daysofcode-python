#!/usr/bin/evn python3

from turtle import Screen
from time import sleep

from player import Player
from scoreboard import Scoreboard
from car import Car

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

if __name__ == '__main__':
    screen.listen()
    screen.onkeypress(player.move, 'Up')
    cars = [Car() for n in range(20)]

    running = True
    loop = 0
    while running:
        screen.update()
        sleep(0.05)
        if loop % 5 == 0 and cars[-1].xcor() < -280:
            cars = [Car() for n in range(20)]

        for car in cars:
            car.move()

        if player.ycor() > 280:
            scoreboard.next_level()
            player.next_level()

        loop += 1

screen.exitonclick()
