#!/usr/bin/evn/python3
from turtle import Screen, shape
from pandas import read_csv

WIDTH = 725
HEIGHT = 491

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
            if ans.capitalize() == state:
                correct_guesses.append(ans)

    screen.exitonclick()
