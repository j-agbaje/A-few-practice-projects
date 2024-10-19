import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create a turtle player
player = Player()
scoreboard = Scoreboard()
scoreboard.write_level()
cars_list = []
for i in range(0, 35):
    new_car = CarManager()
    cars_list.append(new_car)

# Player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    for cars in cars_list:
        cars.move()
        """
        if a car reaches the end of the screen on the left side,it goes back to a random location on the right side,
        to give an infinite loop of cars"""
        if cars.xcor() < -310:
            cars.x = random.randint(280, 2000)
            cars.y = random.randint(-250, 250)
            cars.goto(cars.x, cars.y)

        # Detect player contact with cars
        if player.distance(cars) < 23:
            game_is_on = False
            scoreboard.game_over()

    # Detect player crosses the finish line
    if player.ycor() > 300:
        player.goto(0, -280)
        scoreboard.levels += 1
        scoreboard.write_level()
        for cars in cars_list:
            cars.increase_speed()

screen.exitonclick()
