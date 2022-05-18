#!/usr/bin/env python3

def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(20, 340, 3, 56))
print(add(32, 45, 4))
print(add(7, 3))

