import turtle
from turtle import Turtle
import random

MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

turtle.colormode(255)


def random_rgb_color():
    r = random.randint(50,255)
    g = random.randint(50, 255)
    b = random.randint(50, 255)
    return (r, g, b)


class Ball():

    def __init__(self):
        self.create_ball()
        self.ball.setheading(random.randrange(-55, 55, 20))
        self.move_speed = 0.05


    def create_ball(self):
        self.ball = Turtle('circle')
        self.ball.pu()
        self.ball.color(random_rgb_color())

    def move(self):
        self.ball.fd(MOVE_DISTANCE)

    def paddle_hit(self):
        self.ball.seth((540 - self.ball.heading())%360)
        self.speed_up()

    def bounce_wall(self):
        self.ball.seth(360 - self.ball.heading())

    def reset_position(self):
        self.ball.goto(0,0)
        self.ball.setheading(self.ball.heading() - (random.randrange(-55, 55, 20)))
        self.move_speed = 0.05

    def speed_up(self):
        self.move_speed *= 0.9