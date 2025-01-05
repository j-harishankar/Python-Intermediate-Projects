import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_list = [rock ,paper ,scissors]
user_input = int(input("What do you choose?\nType 0 for rock\n1 for paper\n2 for scissors")) 
computer_input  = random.randint(0,2)
print("User choose:")
print(game_list[user_input])
print("Computer choose")
print(game_list[computer_input])

if user_input==computer_input :
    print("Game draw")
else:
    if user_input == 0 and computer_input == 2:
        print("You Won")
    elif computer_input == 0 and user_input == 2:
        print("You Lose")
    elif user_input < computer_input:
        print("You Lose")    
    elif user_input > computer_input:
        print("You Win")
        

        
 
