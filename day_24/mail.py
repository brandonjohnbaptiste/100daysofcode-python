#!/usr/bin/env python3

with open('input/letters/starting_letter.txt') as file:
    data = file.read()
    letter_starter = data.replace('[', '').replace(']', '')

with open('input/names/invited_names.txt') as names:
    name_lst = [name.strip() for name in names]
    print(name_lst)

for name in name_lst:
    left_index = data.index('[') + 1
    right_index = data.index(']')
    letter = letter_starter.replace(data[left_index:right_index], name)

    with open(f'output/letter_for_{name}', 'w') as final_letter:
        final_letter.write(letter)
