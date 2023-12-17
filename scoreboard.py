from turtle import Turtle
FONT_TYPE = ("Verdana", 15, "normal")
ALIGNMENT = "center"
START_POS = (0, 270)
TEXT_COLOR = "white"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color(TEXT_COLOR)
        self.hideturtle()
        self.penup()
        self.goto(START_POS)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score : {self.score}", font=FONT_TYPE, align=ALIGNMENT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def display_game_over(self):
        self.home()
        self.write("Game Over", font=FONT_TYPE, align=ALIGNMENT)

