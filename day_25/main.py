#!/usr/bin/env python3

from pandas import read_csv

if __name__ == '__main__':
    data = read_csv('weather_data.csv')
    data_dict = data.to_dict()
    print(data_dict)

    temp = data['temp'].to_list()
    print(temp)
