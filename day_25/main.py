#!/usr/bin/env python3
from pandas import read_csv, DataFrame

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

    csv_data = {
        'Fur Colour': ['Black', 'Gray', 'Cinnamon'],
        'Count': [count for count in fur_colours.values()]
    }
    formatted_data = DataFrame(csv_data)
    formatted_data.to_csv('fur_count.csv')



