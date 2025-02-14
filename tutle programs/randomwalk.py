from turtle import * 
from random import *
timmy = Turtle()
screen = Screen()
direction = [0,90,270,180]
for j in range(100):
    timmy.forward(100)
    timmy.right(choice(direction))

screen.exitonclick()