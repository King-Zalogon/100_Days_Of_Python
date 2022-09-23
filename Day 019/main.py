from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=900, height=600)
user_bet = screen.textinput(title="Make your bet", prompt="Enter the name of the turtle you want to bet on: ")
racers = [['leonardo', 'blue', 150], ['donatello', 'indigo', 50], ['rafael', 'red', -50], ['michelangelo', 'orange',
                                                                                           -150]]
tmnt = {'blue': 'leonardo', 'indigo': 'donatello', 'red': 'rafael', 'orange': 'michelangelo'}
all_turtles = []

for i in racers:
    i[0] = Turtle(shape='turtle')
    i[0].color(i[1])
    i[0].pu()
    i[0].goto(x=-400, y=i[2])
    all_turtles.append(i[0])


# leonardo = Turtle(shape='turtle')
# leonardo.color('blue')
# leonardo.pu()
# leonardo.goto(x=-400, y=150)
#
# donatello = Turtle(shape='turtle')
# donatello.color('indigo')
# donatello.pu()
# donatello.goto(x=-400, y=50)
#
# rafael = Turtle(shape='turtle')
# rafael.color('red')
# rafael.pu()
# rafael.goto(x=-400, y=-50)
#
# michelangelo = Turtle(shape='turtle')
# michelangelo.color('orange')
# michelangelo.shape('turtle')
# michelangelo.pu()
# michelangelo.goto(x=-400, y=-150)


def move_forwards(t):
    t.fd(10)


def move_backwards(t):
    t.bk(10)


def turn_left(t):
    t.lt(10)


def turn_right(t):
    t.rt(10)


def clear(t):
    t.clear()
    t.pu()
    t.home()
    t.pd()


def movement():
    screen.onkey(key='Up', fun=move_forwards)
    screen.onkey(key='Down', fun=move_backwards)
    screen.onkey(key='Left', fun=turn_left)
    screen.onkey(key='Right', fun=turn_right)
    screen.onkey(key='c', fun=clear)


if user_bet:
    race_is_on = True

while race_is_on:
    winner = ''
    for t in all_turtles:
        random_distance = random.randint(0, 10)
        t.fd(random_distance)
        if t.xcor() >= 400:
            winner = t.pencolor()
            if tmnt[winner] == user_bet.lower():
                print(f'You won! {tmnt[winner].capitalize()} finished first!')
                race_is_on = False
            else:
                print(f"{tmnt[winner].capitalize()} finished first, but your bet was on {user_bet.capitalize()}")
                print('You lose...')
                race_is_on = False


screen.listen()


screen.exitonclick()
