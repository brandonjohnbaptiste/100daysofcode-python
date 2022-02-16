#!/usr/bin/env python3

from pandas import read_csv

if __name__ == '__main__':
    data = read_csv('Squirrel_Census.csv')

    colours = data['Primary Fur Color']

    fur_colours = {
        'Black': 0,
        'Gray': 0,
        'Cinnamon': 0
    }

    for colour in colours:
        if colour in fur_colours:
            fur_colours[colour] += 1

    print(fur_colours)



