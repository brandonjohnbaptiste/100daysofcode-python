#!/usr/bin/evn/python3
import turtle
from turtle import Screen

if __name__ == '__main__':
    screen = Screen()
    screen.title('U.S. States Quiz')

    image = 'blank_states_img.gif'
    screen.addshape(image)

    turtle.shape(image)

    screen.exitonclick()
