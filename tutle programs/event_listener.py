from turtle import *
tim = Turtle()
screen = Screen()
def move_forward():
    tim.forward(10)
screen.listen()
screen.onkey(fun=move_forward,key="space")
screen.exitonclick()