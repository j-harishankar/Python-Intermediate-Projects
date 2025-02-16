from turtle import * 
from random import *
timmy = Turtle()
screen = Screen()
colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return  (r,g,b)


direction = [0,90,270,180]
timmy.pensize(15)
timmy.speed("fastest")
for j in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(choice(direction))
screen.exitonclick()
