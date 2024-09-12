import random
from celebs_data import data
import art
import os

clear= lambda:os.system('clear')


def picking_celebrity():
    return random.choice(data)


def comparing(celeb_1,celeb_2):
    if celeb_1['follower_count']>celeb_2['follower_count'] or celeb_1['follower_count']==celeb_2['follower_count']:
        return 'a'
    else:
        return 'b'
    
def play():
    celebrity_1=picking_celebrity()
    celebrity_2=picking_celebrity()
    end=False
    score=0

    
    while not end:
        print(art.logo)
        if score>0:
            print(f"You are right! Current score: {score}")
        celebrity_2=picking_celebrity()
        print(f"Compare A: {celebrity_1['name']}, a {celebrity_1['description']}, from {celebrity_1['country']}.{celebrity_1['follower_count']}")
        print(art.vs)
        print(f"Compare B: {celebrity_2['name']}, a {celebrity_2['description']}, from {celebrity_2['country']}.{celebrity_2['follower_count']}")
        guess=input('Who has more followers? Type "A" or "B": ').lower()


        winner=comparing(celebrity_1,celebrity_2)


        if winner==guess:
            if celebrity_2['follower_count']>celebrity_1['follower_count']:
                celebrity_1=celebrity_2
            score+=1
            clear()
        else:
            clear()
            print(art.logo)
            print(f"That's wrong. Final score: {score}")
            end=True


play()

    
        




