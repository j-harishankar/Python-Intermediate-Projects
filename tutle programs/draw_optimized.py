from turtle import *
tim = Turtle()
screen = Screen()
angle = 0



def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def move_right():
    newheading = tim.heading()+10
    tim.setheading(newheading)# we use paranthesis since we actually need the return value
def move_left():
        newheading = tim.heading()-10
        tim.setheading(newheading)
    
screen.listen()
screen.onkeypress(fun=move_forward,key="w")# we dont use paranthesis since it just calls the function
screen.onkeypress(fun=move_backward,key="s")
screen.onkeypress(fun=move_left,key="a")
screen.onkeypress(fun=move_right,key="d")


screen.exitonclick()