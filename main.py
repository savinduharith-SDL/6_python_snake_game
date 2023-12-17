from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen._root.resizable(False, False)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Initialize the key bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_block()
        scoreboard.increase_score()
    x_val = snake.head.xcor()
    y_val = snake.head.ycor()
    if x_val > 280 or x_val < -280 or y_val > 280 or y_val < -280 or snake.is_collision_happened():
        game_is_on = False
        scoreboard.display_game_over()

screen.exitonclick()
