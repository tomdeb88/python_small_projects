import random

random_num=random.randint(0,101)
end=False

print("I'm thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty.Type 'easy' or 'hard':").lower()

if difficulty=='easy':
    attempts=10
elif difficulty=='hard':
    attempts=5

def compare(num):
    global attempts,end
    if num<random_num:
        print("too low")
        attempts-=1

    elif num >random_num:
        print("too high")
        attempts-=1

    elif num==random_num:
        print(f"You git it! The number is {random_num}")
        end=True
        exit()
   


while not end:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    compare(guess)
    if attempts==0:
        print(f'Game over.Number is {random_num}')
        end=True



