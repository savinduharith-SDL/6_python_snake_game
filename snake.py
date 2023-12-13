from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments = []
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
        self.segments[0].forward(20)
        self.segments[0].left(90)

