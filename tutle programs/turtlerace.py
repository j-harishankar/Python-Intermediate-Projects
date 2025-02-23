# ==================================================
# Program: Turtle race
# Description: This program creates multiple turtle you can bet on a turtle just like a horse race
# Date: February 23, 2025
# ==================================================


from turtle import *


# tom = Turtle(shape = "turtle")
# rom = Turtle(shape = "turtle")
# ram = Turtle(shape = "turtle")
# bum = Turtle(shape = "turtle")

colors = ["red","orange","blue","green","purple"]
y_axis = [50,0,-50,-100,-150]
screen = Screen()
screen.setup(width = 500,height = 400)
screen.textinput(title = "Enter your bet",prompt = "Which turtle you will bet? Enter color:")
for i in range(5):
    tim = Turtle(shape = "turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-230,y=y_axis[i])#since screen size is 500,400 we take half to reach the edge


# tom.penup()
# tom.color(colors[1])
# tom.goto(x=-230,y=0)

# rom.penup()
# rom.color(colors[2])
# rom.goto(x=-230,y=-50)

# ram.penup()
# ram.color(colors[3])
# ram.goto(x=-230,y=-100)

# bum.penup()
# bum.color(colors[4])
# bum.goto(x=-230,y=-150)

screen.exitonclick()