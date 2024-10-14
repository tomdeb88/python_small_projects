from turtle import Screen
from snake import Snake
from snack import Food
from score import Score
import time
from sounds import Sound

screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.register_shape("img/strawberry.gif")
screen.register_shape("img/snake_head.gif")
screen.colormode(255)

snake=Snake()
snack=Food()
score=Score()
sound=Sound()


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

    #taking the snack
    if snake.head.distance(snack)< 20:
        snack.food_location()
        snake.prolongate_snake()
        score.add_point()
        sound.eating_sound()

    # hitting the wall
    if snake.head.xcor()<-290 or snake.head.xcor()>290 or snake.head.ycor()<-290 or snake.head.ycor() > 290:
        game_is_on=False
        score.game_over()
        sound.game_over()

    # hitting the tail
    for part in snake.parts[1:]:
        if snake.head.distance(part.position()) < 15:
            game_is_on=False
            score.game_over()
            sound.game_over()







screen.exitonclick()






    


























screen.exitonclick()