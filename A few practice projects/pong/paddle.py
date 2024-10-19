from turtle import Turtle, Screen

screen = Screen()


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.paddle_segments = []
        self.positions = [(-350, 0), (-350, -20), (-350, -40), (-350, -60)]

    def create(self):
        for position in self.positions:
            segment = Turtle()
            segment.color("white")
            segment.shape("square")
            segment.penup()
            segment.goto(position)
            self.paddle_segments.append(segment)

    def up(self):
        if self.paddle_segments[0].ycor() < 270:
            for segment in self.paddle_segments:
                segment.sety(segment.ycor() + 20)

    def down(self):
        if self.paddle_segments[-1].ycor() > -270:
            for segment in self.paddle_segments:
                segment.sety(segment.ycor() - 20)


