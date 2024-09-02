import random

random_num=random.randint(0,101)

print("I'm thinking of a number between 1 and 100")
difficulty=input("Choose a difficulty.Type 'easy' or 'hard':").lower()

if difficulty=='easy':
    attempts=10
elif difficulty=='hard':
    attempts=10


