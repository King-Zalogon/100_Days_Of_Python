import turtle
from turtle import Turtle, Screen
import random
import math
import colorgram



rgb_colors = []
colors = colorgram.extract('er15O.jpg', 300)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
print(len(rgb_colors))

