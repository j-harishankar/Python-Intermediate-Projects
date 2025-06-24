from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("US State Guessing Game")

image = 'blank_states_img.gif'
screen.addshape(image)

bg = Turtle()
bg.shape(image)

data = pd.read_csv("50_states.csv")
data_lst = data['state'].to_list()



guessed_state = []
while len(guessed_state)<=50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 found correct", prompt="Enter a state name:")
    org_ans = answer_state.strip().title()
    if org_ans in data_lst:
        guessed_state.append(org_ans)
        location = data[data.state == org_ans]
        
        x = location.x.item() # new method used to avoid index and retrive the item in csv
        y = location.y.item()

        t = Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(location.iloc[0]['state'], align="center", font=("Arial", 10, "normal"))
    else:
        print(f"State '{answer_state}' not found in CSV.")

screen.exitonclick()
