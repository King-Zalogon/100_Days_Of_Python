import turtle
from turtle import Turtle, Screen
import random
import math
import colorgram

leo = Turtle()
leo.shape('turtle')
leo.color('blue')
leo.pensize(2)
leo.speed(10)
turtle.colormode(255)
directions = [0, 60, 120, 180, 240, 300]
color_range = [(200, 156, 118), (139, 91, 62), (227, 203, 137), (198, 98, 74), (161, 135, 80), (76, 41, 20), (238, 172, 155), (136, 158, 187), (175, 147, 154), (82, 105, 124), (115, 90, 99) , (112, 46, 30), (93, 68, 24), (92, 109, 96), (145, 160, 147), (165, 107, 116), (110, 124, 156), (221, 174, 180), (61, 34, 41), (177, 187, 216), (36, 51, 65), (90, 50, 56), (112, 138, 121), (95, 140, 153), (178, 202, 177), (36, 51, 40), (50, 60, 86), (26, 78, 93), (42, 75, 65), (165, 201, 208)]

# rgb_colors = []
# colors = colorgram.extract('The four Seasons.jpg', 34)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)


def daemon_heister(t, color_list, dots_per_row, dot_width):
    t.pu()
    x = -280
    y = -250
    width = dot_width
    step = dot_width*2
    t.setpos(x, y)

    for z in range(dots_per_row):
        t.setpos(x, (y+(step*z)))
        for _ in range(dots_per_row):
            t.color(random.choice(color_list))
            t.dot(width)
            t.fd(step)
    t.hideturtle()

# daemon_heister(leo, color_range, 7, 40)

def daemian_heistest(t, color_list, n, dot_width):
    t.pu()
    width = dot_width
    step = dot_width*2
    for i in range(n):
        t.lt(90)
        t.color(random.choice(color_list))
        t.dot(width)
        t.fd(step)
        for k in range(int(i/2)):
            t.color(random.choice(color_list))
            t.dot(width)
            t.fd(step)
    t.hideturtle()

daemian_heistest(leo, color_range, 17, 30)

screen = Screen()
screen.exitonclick()
