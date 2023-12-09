import random



#choosing a word
word_list=['ardvark','baboon','camel']
chosen_word=word_list[random.randint(0,len(word_list)-1)]
print(chosen_word)

#get user's guess

guessed_letter=input('Guess a letter: ').lower()

#check if the letter is in guessed word
for l in chosen_word:
    if guessed_letter==l:
        print('right')
    else:
        print('wrong')


display=[]
for _ in range(len(chosen_word)):
    display.append('_')
print(display)

for index,letter in enumerate(chosen_word):
    if guessed_letter==letter:
        display[index]=letter

print(display)