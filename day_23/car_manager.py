#!/usr/bin/evn python3
from car import Car
from turtle import Turtle

CLUSTER_SIZE = 10


class CarManager(Turtle):
    def __init__(self, level):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.cars = []
        self.create_car_cluster()
        self.move_speed = 5
        self.level = level

    def create_car_cluster(self):
        self.cars = [Car() for n in range(CLUSTER_SIZE)]

    def move_cluster(self):
        for car in self.cars:
            car.move(self.move_speed + (5 * self.level))

    def next_level(self):
        self.move_speed += 5
        for car in self.cars:
            car.clear()

