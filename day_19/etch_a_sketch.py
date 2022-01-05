#!/usr/bin/evn python3

from turtle import Turtle, Screen, clearscreen

turtle = Turtle()
turtle.speed(0)
screen = Screen()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def move_left():
    turtle.left(10)


def move_right():
    turtle.right(10)


def clear_screen():
    turtle.clear()


if __name__ == '__main__':
    screen.listen()
    screen.onkeypress(key='w', fun=move_forward)
    screen.onkeypress(key='s', fun=move_backward)
    screen.onkeypress(key='a', fun=move_left)
    screen.onkeypress(key='d', fun=move_right)
    screen.onkeypress(key='c', fun=clear_screen)
    screen.exitonclick()


