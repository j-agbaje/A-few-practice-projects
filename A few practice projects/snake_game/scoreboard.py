from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            contents = file.read()
            file_int = int(contents)
        self.high_score = file_int
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.create()
        self.hideturtle()

    def create(self):
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def keep_score(self):
        self.clear()
        self.create()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.keep_score()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", False, ALIGNMENT, ("Courier", 15, "normal"))
