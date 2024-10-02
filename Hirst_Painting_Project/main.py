# import colorgram
from turtle import Turtle,Screen
import random

# colors=colorgram.extract('image.jpg',15)
#
# list_of_colors=[]
#
#
#
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     color_tuple=(r,g,b)
#     list_of_colors.append(color_tuple)

color_list=[(199, 175, 117), (125, 36, 24), (187, 158, 51), (170, 106, 56), (6, 57, 83), (222, 223, 225),
            (199, 215, 204),(108, 67, 85), (88, 142, 56), (20, 122, 175), (110, 160, 175), (76, 39, 48)]

tim=Turtle()
screen=Screen()
screen.colormode(255)
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
tim.pendown()

def dots(dot_size,gape,row,columns):
    x=1
    y=gape
    position = tim.position()
    while x<=row:

        for i in range(columns):
            color=random.choice(color_list)
            tim.dot(dot_size,color)
            tim.penup()
            tim.forward(gape)
        tim.setposition(position[0],position[1]+y)
        y+=gape
        x+=1

dots(20,50,7,7)







screen.exitonclick()