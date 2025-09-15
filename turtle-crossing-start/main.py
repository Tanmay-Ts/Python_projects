import time
from turtle import Screen,Turtle
import random

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car = CarManager()
player = Player()
screen.listen()
screen.onkey(player.move,"Up")
scoreboard= Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 6) == 1:  # 1 in 6 chance every 0.1s
        car.create_new_car()
    car.move_car()
    for each_car in car.all_cars:
        if player.distance(each_car) < 20:
            scoreboard.game_over()
            game_is_on = False
screen.exitonclick()


