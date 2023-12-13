from turtle import Turtle

MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.initialize_snake()
        self.head = self.segments[0]

    def initialize_snake(self):
        for i in range(3):
            xpos = i * (-20)
            new_block = Turtle(shape="square")
            new_block.penup()
            new_block.goto(xpos, 0)
            new_block.color("white")
            self.segments.append(new_block)
    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.segments[0].forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

