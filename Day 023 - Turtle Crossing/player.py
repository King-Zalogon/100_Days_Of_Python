from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        self.shape = "turtle"
        super(Turtle).__init__()
        self.create_turtle()

    def create_turtle(self):
        self.turtle = Turtle('turtle')
        self.turtle.color('green')
        self.turtle.pu()
        self.turtle.lt(90)

    def move(self):
        self.turtle.fd(MOVE_DISTANCE)

    def reset_position(self):
        self.turtle.goto(STARTING_POSITION)

    def road_kill(self):
        self.turtle.shapesize(3, 1)
        self.turtle.color('red')
