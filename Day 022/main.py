from turtle import Screen
from ball import Ball
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')

game_is_on = True
ball = Ball()

while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.move()

    if ball.ball.pos()[0] >= 350 and (ball.ball.heading() < 90 or ball.ball.heading() >= 270):
        ball.bounce_left()

    elif ball.ball.pos()[0] <= -350 and 90 < ball.ball.heading() < 270:
        ball.bounce_right()

    elif ball.ball.pos()[1] >= 250 and 0 < ball.ball.heading() < 180:
        ball.bounce_down()

    elif ball.ball.pos()[1] <= -250 and 180 < ball.ball.heading() < 360:
        ball.bounce_up()



screen.exitonclick()
