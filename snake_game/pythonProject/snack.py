import random
from turtle import Turtle


class Snack:
    def __init__(self):
        self.x_pos=random.randint(-280,280)
        self.y_pos=random.randint(-280,280)
        self.create_snack()

    def create_snack(self):
        snack=Turtle('circle')
        snack.penup()
        snack.color('red')
        snack.goto(self.x_pos,self.y_pos)