from turtle import Screen,Turtle

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")

for i in range(3):
    xpos = i*(-20)
    new_turtle = Turtle(shape="square")
    new_turtle.penup()
    new_turtle.goto(xpos,0)
    new_turtle.color("white")

screen.exitonclick()