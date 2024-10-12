from turtle import Screen
from snake import Snake
from snack import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
snack=Food()
score=Score()


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

    print(snake.head.distance(snack))
    if snake.head.distance(snack)< 15:
        print('omomom')
        snack.food_location()
        score.add_point()






screen.exitonclick()






    


























screen.exitonclick()