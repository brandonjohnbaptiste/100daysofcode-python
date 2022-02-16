#!/usr/bin/evn/python3
from turtle import Screen, shape, Turtle
from pandas import read_csv

WIDTH = 725
HEIGHT = 491


def display_correct_state(state):
    state_data = read_csv('50_states.csv')
    x_cor = int(state_data[state_data.state == state].x)
    y_cor = int(state_data[state_data.state == state].y)

    state_name = Turtle()
    state_name.penup()
    state_name.hideturtle()
    state_name.goto(x_cor, y_cor)
    state_name.write(f'{state}', font=('Courier', 15, 'normal'))


if __name__ == '__main__':
    data = read_csv('50_states.csv')
    states = data['state']

    screen = Screen()
    screen.title('U.S. States Quiz')
    screen.setup(WIDTH, HEIGHT)

    correct_guesses = []
    guessing = True

    image = 'blank_states_img.gif'
    screen.addshape(image)
    shape(image)

    while guessing:
        ans = screen.textinput(title=f'{len(correct_guesses)}/50 States Correct', prompt='Enter the state\'s name')

        for state in states:
            if ans == state:
                correct_guesses.append(ans)
                display_correct_state(state)

            guessing = not len(correct_guesses) == 50

    screen.exitonclick()
