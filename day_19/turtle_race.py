#!/usr/bin/env python3

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle do you think will enter the race? ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def create_turtle(color):
    turtle = Turtle(shape='turtle')
    turtle.color(color)

    return turtle


turtles = [create_turtle(color) for color in colors]

offset = 0
init_x = -230
init_y = -125

for racer in turtles:
    racer.penup()
    racer.setpos(x=init_x, y=(init_y + offset))
    offset += 50

racing = True
while racing:
    for turtle in turtles:
        if turtle.xcor() > 210:
            racing = False
            if user_bet == turtle.pencolor():
                print(f'You\'ve won! The {turtle.pencolor()} turtle was the winner!')
            else:
                print(f'You\'ve lost. The {turtle.pencolor()} turtle was the winner!')

        turtle.forward(randint(0, 10))

screen.exitonclick()
