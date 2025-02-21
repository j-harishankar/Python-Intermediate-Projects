from turtle import *
jimmy = Turtle()
screen = Screen()

def draw(num_of_sides):
    angle = 360/num_of_sides
    for i in range(num_of_sides):
        jimmy.forward(100)
        jimmy.right(angle)
for _ in range(3,10):
    if _%2==0:
        jimmy.color("red")
    else: 
        jimmy.color("green")
    draw(_)
screen.exitonclick()