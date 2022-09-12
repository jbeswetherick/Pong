from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
score = Scoreboard()

is_on = True
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    elif ball.xcor() > 390:
        ball.reset_position()
        score.l_point()
    elif ball.xcor() < -390:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
