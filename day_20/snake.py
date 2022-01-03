#!/usr/bin/evn3 python3
from turtle import Turtle


def create_body_part():
    t = Turtle(shape='square')
    t.color('white')
    t.penup()
    return t


class Snake:
    def __init__(self):
        self.snake_body = [create_body_part() for i in range(3)]

        init_x = 0
        init_y = 0
        offset = 20

        for part in self.snake_body:
            part.setpos(x=(init_x - (offset * self.snake_body.index(part))), y=init_y)

    def move(self):
        for part_index in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part_index - 1].xcor()
            new_y = self.snake_body[part_index - 1].ycor()
            self.snake_body[part_index].goto(x=new_x, y=new_y)

        self.snake_body[0].forward(20)
