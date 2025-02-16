from turtle import * 
from random import *
timmy = Turtle()
screen = Screen()
colors = ["Red","Blue","Gray","Cyan","Magenta","Lime","Maroon","Navy","Olive","Teal","Aqua","Fuchsia","Silver"]
direction = [0,90,270,180]
timmy.pensize(15)
timmy.speed("fastest")
for j in range(200):
    timmy.color(choice(colors))
    timmy.forward(30)
    timmy.setheading(choice(direction))
screen.exitonclick()