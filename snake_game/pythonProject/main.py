from turtle import Screen
from snake import Snake
from snack import Snack
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake=Snake()
snack=Snack()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    screen.onkey(snake.up,'Up')
    screen.onkey(snake.down,'Down')
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')

    if snake.head.xcor()==-300 or snake.head.xcor()==300:
        game_is_on=False
    if snake.head.ycor()==-300 or snake.head.ycor()==300:
        game_is_on=False


screen.exitonclick()






    


























screen.exitonclick()