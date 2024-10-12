from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-30, 270)
        self.color('white')
        self.points=0
        self.write(f"Score: {self.points}",font=("Arial",18,'normal'))





    def add_point(self):
        self.points+=1
        self.clear()
        self.write(f"Score: {self.points}", font=("Arial", 18,'normal'))



