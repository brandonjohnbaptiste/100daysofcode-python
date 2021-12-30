#!/usr/bin/env python3

from turtle import Turtle, Screen

screen_height = 600
screen_width = 600

screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)


def create_body_part():
    t = Turtle(shape='square')
    t.color('white')
    t.penup()
    return t


snake_body = [create_body_part() for i in range(3)]
init_x = 0
init_y = 0
offset = 20

for part in snake_body:
    part.setpos(x=(init_x - (offset * snake_body.index(part))), y=init_y)

if __name__ == '__main__':
    game_running = True
    while game_running:
        for part in snake_body:
            part.forward(1)
        screen.update()

screen.exitonclick()
