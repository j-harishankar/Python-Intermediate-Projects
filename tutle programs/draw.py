# ==================================================
# Program: Turtle Movement
# Description: This program controls the movement of a turtle using WASD.
# Date: February 22, 2025
# ==================================================



from turtle import *
tim = Turtle()
screen = Screen()
angle = 0


def right_angle():
    global angle 
    angle = angle+5
    return angle
def left_angle():
    global angle           
    angle = angle-5
    return angle
def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_right():
    tim.right(right_angle())# we use paranthesis since we actually need the return value
def move_left():
    tim.left(left_angle())
    
screen.listen()
screen.onkeypress(fun=move_forward,key="w")# we dont use paranthesis since it just calls the function
screen.onkeypress(fun=move_backward,key="s")
screen.onkeypress(fun=move_left,key="a")
screen.onkeypress(fun=move_right,key="d")


screen.exitonclick()