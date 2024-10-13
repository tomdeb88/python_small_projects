import random
from turtle import Turtle



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("img/strawberry.gif")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed('fastest')
        self.food_location()

    def food_location(self):
        x_position=random.randint(-275,275)
        y_position=random.randint(-275,275)
        self.goto(x_position,y_position)


