from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.levels = 1
        self.penup()
        self.goto(-240, 270)
        self.hideturtle()

    def write_level(self):
        self.clear()
        self.write(f"Level:{self.levels}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)

