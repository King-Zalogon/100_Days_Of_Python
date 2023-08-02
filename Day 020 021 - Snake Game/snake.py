import turtle
from turtle import Turtle
import random

MOVE_DISTANCE = 20
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


class Snake:
    def __init__(self):
        self.length = 3
        self.body_color = random_rgb_color()
        self.start_x = -5
        self.start_y = +1
        self.snake_body = []
        self.create_snake()


    def create_snake(self):
        snake_head = Turtle('triangle')
        snake_head.color(self.body_color)
        snake_head.pu()
        snake_start = snake_head.setpos(self.start_x, self.start_y)
        self.snake_body.append(snake_head)
        self.head = self.snake_body[0]


        for n in range(self.length):
            self.add_seg(n)


    def move(self):
        for seg_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg_num - 1].xcor()
            new_y = self.snake_body[seg_num - 1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)

        self.head.fd(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_seg(self, n):
        segment = Turtle('square')
        segment.color(random_rgb_color())
        segment.pu()
        segment.goto(x=(self.start_x - (20 * (n + 1))), y=self.start_y)
        self.snake_body.append(segment)

    def extend(self):
        segment = Turtle('square')
        segment.color(random_rgb_color())
        segment.pu()
        segment.goto(self.snake_body[-1].position())
        self.snake_body.append(segment)

    def reset_snake(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
