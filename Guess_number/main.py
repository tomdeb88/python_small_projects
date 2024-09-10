import random
from art import logo

random_number=random.randint(1,100)
end=False
def game_level():
    difficulty=input('Choose a difficulty.Type "easy" or "hard": ').lower()
    if difficulty=='easy':
        return 10
    elif difficulty=='hard':
        return 5
    else:
        print("Choose difficulty. Try again")
        exit()
def compare(guessing_number,tries):
    user_guess=int(input('Make a guess:'))
    if user_guess<guessing_number:
        print('Too low')
        return tries - 1
    elif user_guess>guessing_number:
        print('Too high')
        return tries -1
    else:
        return 'you win'


print(logo)
print('Welcome to the Number Guessing Game')
print('I am thinking of a number between 1 and 100.')

attempts=game_level()

while not end:
    print(f"You have {attempts} attempts remaining to guess the number")
    attempts=compare(random_number,attempts)
    if attempts==0:
        print(f'You lose.The number is {random_number}')
        end=True
    elif attempts=='you win':
        print(f'You got it! The guessing number is {random_number}')
        end=True
    elif attempts!=0:
        print('Guess again')




