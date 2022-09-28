from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle:

    def __init__(self, x, y):
        self.create_paddle(x, y)

    def create_paddle(self, x, y):
        self.paddle = Turtle('square')
        self.paddle.color('white')
        self.paddle.pu()
        self.paddle.speed('fastest')
        self.paddle.shapesize(5, 1)
        self.paddle.goto(x, y)

    def move_up(self):
        new_y = self.paddle.ycor() + MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)

    def move_down(self):
        new_y = self.paddle.ycor() - MOVE_DISTANCE
        self.paddle.goto(self.paddle.xcor(), new_y)
