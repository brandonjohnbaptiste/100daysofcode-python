#!/usr/bin/env python3

from pandas import read_csv


def avg(lst):
    return sum(lst) / len(lst)


def celsius_to_fahrenheit(value):
    return ((9/5) * value) + 32


if __name__ == '__main__':
    data = read_csv('weather_data.csv')

    temp = data.temp
    avg_temp = temp.mean()
    max_temp = temp.max()
    print(f'The average temperature was: {avg_temp:.2f}')
    print(f'The maximum temperature was: {max_temp}')

    monday = data[data.day == 'Monday']
    monday_temp = int(monday.temp)
    monday_temp_converted = celsius_to_fahrenheit(monday_temp)
    print(f'The temperature on Monday was: {monday_temp_converted}F')



