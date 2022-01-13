#!/usr/bin/evn python3
from car import Car
from turtle import Turtle

CLUSTER_SIZE = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.cars = []
        self.create_car_cluster()

    def create_car_cluster(self):
        self.cars = [Car() for n in range(CLUSTER_SIZE)]

    def move_cluster(self):
        for car in self.cars:
            car.move()
