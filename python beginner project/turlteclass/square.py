from turtle import *

timmy = Turtle()
screen = Screen()
for i in range(4):
    timmy.forward(100)
    timmy.right(90)
    timmy.forward(100)  # Move the turtle forward by 100 units
screen.exitonclick()  # Wait for a click to close the window
