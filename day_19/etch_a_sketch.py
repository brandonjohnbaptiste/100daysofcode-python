#!/usr/bin/evn python3

from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)


if __name__ == '__main__':
    screen.listen()
    screen.onkey(key='space',fun=move_forward)
    screen.exitonclick()