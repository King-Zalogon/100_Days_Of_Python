import time
import turtle
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
turtle.colormode(255)


def random_color():
    r = random.randrange(50, 200)
    g = random.randrange(50, 200)
    b = random.randrange(50, 200)
    color = (r, g, b)
    return color


class CarManager(Turtle):

    def __init__(self):
        super(Turtle).__init__()
        self.traffic = []

    def create_car(self):
        self.car = Turtle("square")
        self.car.pu()
        self.car.shapesize(1, 2)
        self.car.goto(320, random.randrange(-240, 260, 40))
        self.car.color(random_color())
        self.traffic.append(self.car)

    def car_move(self):
        for car in self.traffic:
            car.bk(STARTING_MOVE_DISTANCE)
