import random



#choosing a word
word_list=['ardvark','baboon','camel']
chosen_word=word_list[random.randint(0,len(word_list)-1)]
print(chosen_word)

#get user's guess

guessed_letter=input('Guess a letter: ').lower()

#check if the letter is in guessed word

if guessed_letter in chosen_word:
    print('yes')
