
from turtle import Screen
from paddle import Paddle
import time
from scoreboard import Scoreboard
from ball import Ball

screen = Screen()

screen.bgcolor("black")
screen.tracer(0)
screen.setup (width=800, height=600, startx=None, starty=None)
screen.title("pong")
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
new_ball = Ball()
scoreboard = Scoreboard()





screen.listen()
screen.onkey(r_paddle.turn_left,"Up")
screen.onkey(r_paddle.turn_right,"Down")
screen.onkey(l_paddle.turn_left,"w")
screen.onkey(l_paddle.turn_right,"s")

is_on = True
while is_on:
    time.sleep(0.09)
    screen.update()
    new_ball.move()

    if new_ball.ycor() > 280 or new_ball.ycor() < -280:
        new_ball.bounce_y()
    if (new_ball.distance(r_paddle) < 50 and new_ball.xcor() > 320) or \
        (new_ball.distance(l_paddle) < 50 and new_ball.xcor() < -320):
            new_ball.bounce_x()

    if new_ball.xcor() >= 400:
        new_ball.reset_position()
        scoreboard.l_point()

    if new_ball.xcor() <= -400:
        new_ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()

