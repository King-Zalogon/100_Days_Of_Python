from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(900, 600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle_l = Paddle(-350, 0)
paddle_r = Paddle(350, 0)
score = ScoreBoard()
ball = Ball()

game_is_on = True
screen.listen()

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    screen.onkeypress(paddle_r.move_up, 'Up')
    screen.onkeypress(paddle_r.move_down, 'Down')
    screen.onkeypress(paddle_l.move_up, 'w')
    screen.onkeypress(paddle_l.move_down, 's')

    if ball.ball.distance(paddle_l.paddle.pos()) < 50 and ball.ball.xcor() < -325:
        ball.paddle_hit()

    elif ball.ball.distance(paddle_r.paddle.pos()) < 50 and ball.ball.xcor() > 325:
        ball.paddle_hit()

    elif ball.ball.pos()[1] >= 250 and 0 < ball.ball.heading() < 180:
        ball.bounce_wall()

    elif ball.ball.pos()[1] <= -250 and 180 < ball.ball.heading() < 360:
        ball.bounce_wall()

    if ball.ball.xcor() > 390:
        score.l_point()
        ball.reset_position()

    if ball.ball.xcor() < -390:
        score.r_point()
        ball.reset_position()



screen.exitonclick()
