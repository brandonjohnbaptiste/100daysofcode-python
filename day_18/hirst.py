#!/usr/bin/env python3

from colorgram import extract

colors_objects = extract('hirst.jpeg', 16)
colors = [(color.rgb.r, color.rgb.b, color.rgb.b) for color in colors_objects]
print(colors)
