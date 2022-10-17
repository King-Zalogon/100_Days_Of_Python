from turtle import Turtle
import random
ALIGN = 'center'
FONT = ('Courier', 12, 'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        with open("data.txt") as record:
            self.high_score = record.read()
        self.hideturtle()
        self.pu()
        self.goto(0,280)
        self.color('white')
        self.update_score()


    def update_score(self):
        self.clear()
        with open("data.txt") as record:
            self.high_score = record.read()
        self.write(f'Score: {self.score} - High Score: {self.high_score}', False, ALIGN, FONT)

    def reset_scoreboard(self):
        if self.score > int(self.high_score):
            with open('data.txt', mode= 'w') as record:
                record.write(str(self.score))
        self.score = 0
        self.update_score()

    def scoreup(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER!', False, ALIGN, FONT)