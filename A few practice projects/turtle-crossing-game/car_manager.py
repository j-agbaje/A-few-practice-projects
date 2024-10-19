from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 0.5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.x = random.randint(280, 2000)
        self.y = random.randint(-250, 250)
        self.goto(self.x, self.y)
        self.setheading(180)
        self.car_speed = 1

    def move(self):
        for i in range(0, 10):
            self.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT




