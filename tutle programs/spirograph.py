import turtle as t 
from random import * 
timmy = t.Turtle()
screen = t.Screen()

#random color code
t.colormode(255)
def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return  (r,g,b)#it returns the random color as tuple since the format of the code is color((r,g,b))


timmy.speed("fastest")
def spirograph(size_bw_circles):
    for _ in range(int(360/size_bw_circles)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading+size_bw_circles)
spirograph(1)


screen.exitonclick()