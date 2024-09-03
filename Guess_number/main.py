import random
from art import logo

random_num=random.randint(1,100)
attempts=0
end=False

print(logo)
print("I'm thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty.Type 'easy' or 'hard':").lower()

if difficulty=='easy':
    attempts=10
elif difficulty=='hard':
    attempts=5

def compare(num,attempt):
    if num<random_num:
        print("Too low")
        return attempt-1

    elif num >random_num:
        print("Too high")
        return attempt-1

    elif num==random_num:
        print(f"You got it! The number is {random_num}")
        return "game over"
   


while not end:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    attempts=compare(guess,attempts)
    if attempts==0:
        print(f'Game over.Number is {random_num}')
        end=True
    elif attempts=="game over":
        end=True
    elif guess!=random_num:
        print("Guess again! ")



