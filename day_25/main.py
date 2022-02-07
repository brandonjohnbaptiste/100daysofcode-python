#!/usr/bin/env python3

from pandas import read_csv


def avg(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':
    data = read_csv('weather_data.csv')

    temp = data['temp'].to_list()
    avg_temp = avg(temp)
    print(f'The average temperature was: {avg_temp:.2f}')

