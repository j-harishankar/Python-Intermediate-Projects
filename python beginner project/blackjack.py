import os
import random
my_list = []
com_list = []
comp_score=-1
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(list):
    if sum(list) == 21 and len(list)==2:
        return 0
    if 11 in list and sum(list)>21:
        list.remove(11)
        list.append(1)    
    return sum(list)
def compare(uscore,cscore):
    if uscore == cscore:
        return 'draw'
    elif uscore==0:
        return 'you win'
    elif cscore==0:
        return 'you lose'
    elif uscore>21:
        return'you went over'
    elif cscore>21:
        return 'computer went over'
    elif uscore>cscore:
        return 'you win'
    else:
        return 'you lose'
is_true = True
start = input("do you want to play a game of black jack type 'y' or 'n'")
if start == 'y':
    os.system('cls')
    print('###############BLACK JACK#################')
    for _ in range(2):
        my_list.append(deal_card())
        com_list.append(deal_card())
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(my_list)
        comp_score = calculate_score(com_list)
        print(f'user cards:{my_list} and user score is {user_score}')
        print(f'computers first card is {com_list[0]}')
        if user_score==0 or comp_score==0 or user_score>21:
            is_game_over = True
        else:
            choice = input('hit or pass y/n')
            if choice=='y':
                my_list.append(deal_card())
            else:
                is_game_over=True
    while comp_score==0 or comp_score<17:
        com_list.append(deal_card())
        comp_score = calculate_score(com_list)
print(compare(user_score,comp_score))
     
