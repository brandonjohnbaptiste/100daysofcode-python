#!/usr/bin/evn/python3
from turtle import Screen, shape
from pandas import read_csv

if __name__ == '__main__':
    data = read_csv('50_states.csv')
    states = data['state']
    screen = Screen()
    screen.title('U.S. States Quiz')
    screen.setup(725, 491)

    image = 'blank_states_img.gif'
    screen.addshape(image)
    shape(image)

    print(states)
    ans = screen.textinput(title='Guess the state', prompt='Enter the state\'s name')
    screen.exitonclick()
