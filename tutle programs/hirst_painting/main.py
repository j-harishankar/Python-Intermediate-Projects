import turtle
import random


turtle.colormode(255)

timmy = turtle.Turtle()
screen = turtle.Screen()
timmy.speed("fastest")
timmy.penup()
timmy.setheading(225)#to make it go to the right edge of the screen 
timmy.forward(300)#6*50 since it would reach the edge 
timmy.setheading(0)

no_of_dots = 100

color_list = [(250, 249, 247), (243, 246, 250), (244, 251, 248), (252, 244, 248), (219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98), (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102), (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74), (3, 96, 115), (237, 161, 174), (238, 166, 152), (54, 59, 93), (152, 207, 220), (102, 126, 174), (40, 56, 76), (34, 87, 53), (232, 209, 16), (74, 79, 40), (44, 70, 45)]
for dots in range(1,no_of_dots+1):
    timmy.forward(50)
    timmy.dot(20,random.choice(color_list))
    if dots%10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.exitonclick()