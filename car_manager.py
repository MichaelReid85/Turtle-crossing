from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):


    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        # self.color(COLORS)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(350, 0)
        self.move_speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        new_x = self.xcor() - self.move_speed
        self.goto(new_x, self.ycor())

        if self.xcor() < -320:
            self.reset()
            self.penup()
            self.shapesize(stretch_wid=1, stretch_len=2)
            self.goto(350, 0)

    def player_scored(self):
        new_x = STARTING_MOVE_DISTANCE - MOVE_INCREMENT
        self.reset()
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(350, 0)
        self.move_speed += MOVE_INCREMENT


