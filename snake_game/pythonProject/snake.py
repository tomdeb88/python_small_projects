from turtle import Turtle



class Snake:
    def __init__(self):
        self.parts=[]
        self.x_position=0
        self.create_snake()
        self.head=self.parts[0]

    def create_snake(self):
        for i in range(3):
            new_part=Turtle('square')
            new_part.color('white')
            new_part.penup()
            new_part.setposition(self.x_position,y=0)
            self.parts.append(new_part)
            self.x_position-=20
    def move(self):
        for part_position in range(len(self.parts)-1,0,-1):
            new_x_position=self.parts[part_position-1].xcor()
            new_y_position=self.parts[part_position-1].ycor()
            self.parts[part_position].goto(new_x_position,new_y_position)
        self.head.forward(20)

    def up(self):
      if self.head.heading() !=270:
          self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right (self):
        if self.head.heading() != 180:
            self.head.setheading(0)


