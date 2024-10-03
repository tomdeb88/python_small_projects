
from turtle import Turtle,Screen
import random
screen=Screen()
screen.setup(500,400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color(red/blue/yellow/green/orange/black): ").lower()
COLORS=['red','green','yellow','orange','blue','black']
X_POSITION=-240
Y_POSITION=[-20,-60,-100,20,60,100]
is_on=False

turtles=[]

for index in range(6):
    turtle=Turtle(shape='turtle')
    turtle.penup()
    turtle.color(COLORS[index])
    turtle.goto(x=X_POSITION, y=Y_POSITION[index])
    turtles.append(turtle)

if user_bet:
    is_on=True

while is_on:
    for turtle in turtles:
        if turtle.xcor()<230:
            step=random.randint(0,10)
            turtle.forward(step)
        else:
            is_on=False
            winning_color=turtle.color()[0]
            if winning_color==user_bet:
                screen.title(f"You win! {winning_color.capitalize()} won the race")
            else:
                screen.title(f"You lose! {winning_color.capitalize()} won the race")







screen.exitonclick()