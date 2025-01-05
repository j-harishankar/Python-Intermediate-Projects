import hang_words
import hang_ascii
import random

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
print(hang_ascii.logo)
word = random.choice(hang_words.word_list)
print(word) 

answer_list = []
for letter in word:
    answer_list.append('_')
print(f"Answer list is == {answer_list}")
game_over = False
life = 6
guessed = []
while not game_over:
    
    guess = input("guess a letter: ").lower()
    
    for a in range(len(word)):    
        if guess==word[a]:
            answer_list[a] = guess
    if guess in guessed:
        print("Already guessed")
    print(answer_list)
    if guess not in word:
        life-=1
        print(f'''You guessed a word "{guess}" that is not in the word so you lose a life''')
        print(f"{hang_ascii.man[life]}")
    if life == 0:
        game_over = True
        print(" You lose the game")
        print(f" The correct word is {word.upper()}")
  
    if '_' not in answer_list:
        game_over = True
        print(f"{''.join(answer_list)}")
        print("You Won the Game!!!")
    guessed.append(guess) 