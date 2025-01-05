import art
import random
print(art.ascii_art)

def easy(c):
    global n,e,game_over
    if c==n:
        print("You won the game")
        game_over = True
    elif c<n:
        print("the number is too low")
        e=e-1
    else:
        print("The number is too high")
        e=e-1
def hard(c):
    global n,h,game_over
    if c==n:
        print("You won the game")
        game_over = True
    elif c<n:
        print("the number is too low")
        h=h-1
    else:
        print("The number is too high")
        h=h-1
print("welcome to the number guessing game!!!")
print("I think of the number between 1 and 100")
choice=input("choose the hardness level easy or hard")
n = random.choice(range(101))
e=10
h=5
game_over = False
if choice=="easy":
    print("you Have total of 10 lifes")
    while not game_over and e>0:
        k=int(input("enter your guess"))
        print(f"you have {e} lifes remaining")
        easy(k)
    if game_over:
        print("You won!!!")
    else:
        print(f"You lose the number is {n}")
else:
    print("you Have total of 5 lifes")
    while not game_over and h>0:
        k=int(input("enter your guess"))
        print(f"you have {h} lifes remaining")
        hard(k)
    if game_over:
        print("You won!!!")
    else:
        print(f"You lose the number is {n}")