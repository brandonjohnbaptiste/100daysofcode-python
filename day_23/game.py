#!/usr/bin/evn python3

from turtle import Screen
from time import sleep

from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_clusters = [CarManager()]

if __name__ == '__main__':
    screen.listen()
    screen.onkeypress(player.move, 'Up')

    running = True
    loop = 1
    while running:
        screen.update()
        sleep(0.05)

        for cluster in car_clusters:
            cluster.move_cluster()

        if player.ycor() > 280:
            scoreboard.next_level()
            player.next_level()

        if loop % 50 == 0:
            car_clusters.append(CarManager())

        loop += 1
screen.exitonclick()
