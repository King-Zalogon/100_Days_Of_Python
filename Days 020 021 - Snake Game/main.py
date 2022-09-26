from turtle import Turtle, Screen
import time
from snake import Snake_Nest

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Python Game")
screen.tracer(0)

snake_nest = Snake_Nest()
snake = snake_nest.create_snake()

screen.update()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)





# Note to self: Code before this
screen.exitonclick()
