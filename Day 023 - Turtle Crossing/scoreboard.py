from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGN = 'left'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.pu()
        self.goto(-280, 270)
        self.color('black')
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f'Level {self.level}', False, ALIGN, FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER!', False, 'center', FONT)
