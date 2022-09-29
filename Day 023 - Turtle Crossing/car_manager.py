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
        self.speed_factor = 0.1

    def create_car(self):
        self.car = Turtle("square")
        self.car.pu()
        self.car.shapesize(1, 2)
        self.car.goto(320, random.randrange(-240, 260, 20))
        self.car.color(random_color())
        self.traffic.append(self.car)

    def car_move(self):
        time.sleep(self.speed_factor)
        for car in self.traffic:
            car.bk(STARTING_MOVE_DISTANCE)


    def speed_up(self):
        self.speed_factor *= 0.8