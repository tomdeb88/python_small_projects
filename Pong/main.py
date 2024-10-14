from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)


right_paddle=Paddle(350,0)
left_paddle=Paddle(-350,0)

screen.onkey(right_paddle.move_up,'Up')
screen.onkey(right_paddle.move_down,'Down')
screen.onkey(left_paddle.move_up,'w')
screen.onkey(left_paddle.move_down,'s')

game_on=True

while game_on:
    screen.update()













screen.exitonclick()