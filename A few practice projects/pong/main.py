from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


# Function to draw dashes
def draw_dashes():
    dashes = Turtle()
    dashes.color("white")
    dashes.penup()
    dashes.hideturtle()
    dashes.goto(0, 300)
    dashes.setheading(270)  # Pointing downwards
    for i in range(30):  # 25 dashes
        dashes.pendown()
        dashes.forward(10)
        dashes.penup()
        dashes.forward(10)


draw_dashes()

# Set up the paddle
left_paddle = Paddle()
left_paddle.create()
right_paddle = Paddle()
right_paddle.positions = [(350, 0), (350, -20), (350, -40), (350, -60)]
right_paddle.create()
ball = Ball()
scoreboard = Scoreboard()

# Set up key bindings
screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "q")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the Wall
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

        # Detect collision with the right_paddle
    for segment in right_paddle.paddle_segments:
        if ball.distance(segment) < 50 and ball.xcor() > 320 and ball.x_move > 0:
            ball.bounce_x()

        # Detect collision with the left-paddle
    for segment in left_paddle.paddle_segments:
        if ball.distance(segment) < 50 and ball.xcor() < -320 and ball.x_move < 0:
            ball.bounce_x()

    # Detect left paddle miss
    if ball.xcor() >= 420:
        ball.reset()
        scoreboard.l_point()

    # Detect right paddle miss
    if ball.xcor() <= -420:
        ball.reset()
        scoreboard.r_point()

# Keep the screen open
screen.exitonclick()
