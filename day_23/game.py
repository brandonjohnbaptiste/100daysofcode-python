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
car_clusters = [CarManager(0)]

if __name__ == '__main__':
    screen.listen()
    screen.onkeypress(player.move, 'Up')

    running = True
    loop = 1
    level = 0

    while running:
        screen.update()
        sleep(0.05)

        for cluster in car_clusters:
            cluster.move_cluster()
            for car in cluster.cars:
                if player.distance(car) < 20:
                    scoreboard.game_over()
                    running = False

        if player.ycor() > 280:
            scoreboard.next_level()
            player.next_level()
            for cluster in car_clusters:
                cluster.next_level()

            level += 1

        if loop % 25 == 0:
            for i in range(level):
                car_clusters.append(CarManager(level))

        loop += 1
screen.exitonclick()
