from blackjack_logo import logo
import random

cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player_cards=[]
comp_cards=[]



def calculating_score():
    if sum(player_cards)==0 and sum(comp_cards)==0:
        for _ in range(2):
            player_cards.append(random.choice(cards))
            comp_cards.append(random.choice(cards))
    else:
        player_cards.append(random.choice(cards))
    if sum(comp_cards)<=16:
        comp_cards.append(random.choice(cards))


print(logo,"\n\n")

calculating_score()
print(f"Your cards {player_cards},your current score: {sum(player_cards)}")
print(f"Computer's first card:{comp_cards[0],comp_cards}")

if sum(player_cards)==21:
    print("you win")
    print(f"Your cards {player_cards},your current score: {sum(player_cards)}")
    print(f"Computer's first card:{comp_cards}")
elif sum(player_cards)==21 and sum(comp_cards)==21:
    print("It's a draw")
    print(f"Your cards {player_cards},your current score: {sum(player_cards)}")
    print(f"Computer's first card:{comp_cards}")
elif sum(comp_cards)==21:
    print('You lose!')
    print(f"Your cards {player_cards},your current score: {sum(player_cards)}")
    print(f"Computer's first card:{comp_cards}")








    



    
