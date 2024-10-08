from turtle import Screen
from snake import Snake
from snack import Food
import time

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake=Snake()
snack=Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(snack)< 15:
        print('omomom')
        snack.food_location()


screen.exitonclick()






    


























screen.exitonclick()