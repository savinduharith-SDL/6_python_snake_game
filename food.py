from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        rand_x_pos = random.randint(-280, 280)
        rand_y_pos = random.randint(-280, 280)
        self.goto(rand_x_pos, rand_y_pos)

    def refresh(self):
        rand_x_pos = random.randint(-280, 280)
        rand_y_pos = random.randint(-280, 280)
        self.goto(rand_x_pos, rand_y_pos)
