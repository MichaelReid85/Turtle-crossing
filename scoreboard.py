from turtle import Turtle, Screen
ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")

Screen().tracer(0)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-200, 250)
        self.write(arg=f"Score = {self.score}", align="center", font=FONT)

    def safely_across(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)