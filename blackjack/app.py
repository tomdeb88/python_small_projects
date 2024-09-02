import random
from blackjack_logo import logo
import os

clear=lambda:os.system('clear')


def deal_card():
    """picking up a random card"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculating_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)
               
def compare(user_score,comp_score):
    if user_score==comp_score:
        return 'Draw'
    elif comp_score==0:
        return 'You lose'
    elif user_score==0:
        return "You win"
    elif user_score>21:
        return "You went over. You lose"
    elif comp_score>21:
        return "You win,dealer went over"
    elif user_score>comp_score:
        return "You win"
    else:
        return "You lose"
    
def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    user_score=-1
    computer_score=-1
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculating_score(user_cards)
        computer_score=calculating_score(computer_cards)
        print(f"Your cards: {user_cards}, your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            another_card=input("Type 'y' to get another card, type 'n' to pass: ")
            if another_card=='y':
                user_cards.append(deal_card())
            else:
                is_game_over=True

    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculating_score(computer_cards)

    print(f"Your final cards: {user_cards}, your score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, computer's score {computer_score}")
    print(compare(user_score,computer_score))


while input("Do you want to play a game of blackjack? Type 'y' or 'n': ").lower()=='y':
    clear()
    play_game()










