from turtle import Screen,Turtle
import snake
import time

#initializing the screen
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)#switch off the animation

snake = snake.Snake()

game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")
    screen.update()#switch on the animation
    time.sleep(0.1)
    snake.move()





screen.exitonclick()