
from turtle import Turtle,Screen
import random
colors = ["yellow","green","blue","tim","brown"]
tim = Turtle()
blue = Turtle()
green = Turtle()
yellow = Turtle()
brown = Turtle()
blue.shape("turtle")
green.shape("turtle")
yellow.shape("turtle")
brown.shape("turtle")

blue.penup()
green.penup()
yellow.penup()
brown.penup()
blue.color("blue")
green.color("green")
yellow.color("yellow")
brown.color("brown")
go = random.choice(colors)

def ready_set(color,position):
    color.goto(-250,position)





screen = Screen()
tim.shape("turtle")
tim.penup()
tim.color("red")

tim.goto(-250,0)

ready_set(blue,50)
ready_set(green,100)
ready_set(yellow,150)
ready_set(brown,200)






screen.setup(width=500,height=400)
user_guess = screen.textinput(title="place ur bet",prompt="which turtle will win the race" )

if user_guess:
    race_on = True

while race_on:
    for turtle in turtles


screen.exitonclick()