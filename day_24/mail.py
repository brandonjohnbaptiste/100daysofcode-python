#!/usr/bin/env python3

with open('input/letters/starting_letter.txt') as file:
    data = file.read()
    left_index = data.index('[') + 1
    right_index = data.index(']')

    with open('input/names/invited_names.txt') as names:
        name_lst = [name.strip() for name in names]
        print(name_lst)


