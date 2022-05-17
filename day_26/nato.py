#!/usr/bin/env python3
import pandas as pd

nato_alphabet = pd.read_csv('nato_phonetic_alphabet.csv')

nato_dict = dict(nato_alphabet.values)

user_msg = str(input('Enter Your Message: '))
nato_msg = [nato_dict[char.upper()] for char in user_msg]
print(nato_msg)


