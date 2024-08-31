from blackjack_logo import logo
import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def calculating_score():
    player_cards=[]
    for card in range(2):
        player_cards.append(random.choice(cards))
    print(player_cards,sum(player_cards))


will_play=input("Do you want to play a game of Blackjack? type 'y' or 'no': ")

if will_play=='y':
    print(logo,"\n\n")
    calculating_score()

    
else:
    exit()