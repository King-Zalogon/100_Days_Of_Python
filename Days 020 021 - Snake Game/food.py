from turtle import Turtle
import random
from snake import random_rgb_color


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.shape('turtle')
        self.pu()
        self.shapesize(0.5, 0.5)
        self.color(random_rgb_color())
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randrange(-285, 285, 20)
        random_y = random.randrange(-285, 265, 20)
        self.goto(random_x, random_y)
        self.color(random_rgb_color())
