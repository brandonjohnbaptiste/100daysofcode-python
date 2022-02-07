#!/usr/bin/env python3

from pandas import read_csv


def avg(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':
    data = read_csv('weather_data.csv')

    temp = data['temp']
    avg_temp = temp.mean()
    max_temp = temp.max()
    print(f'The average temperature was: {avg_temp:.2f}')
    print(f'The maximum temperature was: {max_temp}')



