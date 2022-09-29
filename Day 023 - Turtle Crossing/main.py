import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


game_is_on = True

player = Player()
player.reset_position()
screen.listen()
screen.onkey(player.move, 'Up')
cars = CarManager()
loop = 0

scoreboard = Scoreboard()

while game_is_on:
    screen.update()
    cars.car_move()
    loop += 1
    if loop%9 == 0:
        cars.create_car()
    else:
        pass

    for car in cars.traffic:
        if player.turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.turtle.ycor() > 260:
        scoreboard.levelup()
        player.reset_position()
        cars.speed_up()



screen.exitonclick()
