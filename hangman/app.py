import random
import hangman_steps
import word_list
import os



print(hangman_steps.logo,'\n\n')

#choosing a word
word_list=word_list.word_list
chosen_word=word_list[random.randint(0,len(word_list)-1)]

display=[]
chances=6
game_run=True
clear=lambda: os.system('clear')

#display covered word
for _ in range(len(chosen_word)):
    display.append(' _ ')

print(f"\n\n{' '.join(display)}\n\n")


while game_run:
    
    
    #get user's guess
    guessed_letter=input('Guess a letter: ').lower()
    clear()
    
    
    #check is it already in display list
    if guessed_letter  in display:
        print("!!! You have already given this letter !!!")
        continue
    

    #check if the letter is in the word and replace underscores with proper letters
    for l in chosen_word:
        if guessed_letter==l:
            for index,letter in enumerate(chosen_word):
                if guessed_letter==letter:
                    display[index]=letter
    
   
    # letter is not int the word

    if guessed_letter not in chosen_word:
        chances-=1
    if chances<6:
        print(hangman_steps.stages[chances])

    print(f"\n\n{''.join(display)}\n\n")
        
   
    # ending game, final statement
    if chances==0:
        print(f'-------> You loose <-------\n\n{chosen_word}')
        game_run=False
    elif " _ " not in display:
        print('-------> You won <-------')
        game_run=False
    














