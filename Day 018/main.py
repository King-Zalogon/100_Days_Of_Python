import turtle
from turtle import Turtle, Screen
import random
import math

leo = Turtle()
leo.shape('turtle')
leo.color('blue')
leo.pensize(2)
leo.speed('fastest')
turtle.colormode(255)
directions = [0, 60, 120, 180, 240, 300]
# colours = ["blue", "green", "red", "dark cyan", "medium violet red", "indigo", "CornflowerBlue", "DarkOrchid",
# "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tup = (r, g, b)
    return my_tup


def polygon(t, n, length):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)


def dashed_line(t, n, length):

    for _ in range(n):
        t.fd(length)
        t.pu()
        t.fd(length)
        t.pd()


def random_walk(t, n, length):

    for _ in range(n):
        t.color(random_color())
        t.fd(length)
        t.setheading(random.choice(directions))


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 180
    length = circumference / n
    polygon(t, n, length)


def rainbow():
    color_list = []
    for i in range(0, 255, 51):
        for j in range(0, 255, 51):
            for k in range(0, 255, 51):
                r = i
                g = j
                b = k
                color_list.append((r, g, b))

    return color_list


my_rainbow = rainbow()


def rainbow_circles(t, color_list, r):
    random.shuffle(color_list)
    radius = range(20, r, 10)
    for i in range(len(color_list)):
        for j in radius:
            t.color(random.choice(color_list))
            circumference = 2 * math.pi * j
            n = 120
            length = circumference / n
            for _ in range(n):
                t.fd(length)
                t.lt(360 / n)

            t.lt(11)


rainbow_circles(leo, my_rainbow, 140)

# Screen
screen = Screen()
screen.exitonclick()
