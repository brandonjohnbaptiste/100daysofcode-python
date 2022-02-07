#!/usr/bin/env python3

from pandas import read_csv


def avg(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':
    data = read_csv('weather_data.csv')
    avg_temp = data['temp'].mean()
    print(f'The average temperature was: {avg_temp:.2f}')


