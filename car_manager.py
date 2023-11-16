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
        # self.color(random.randint.("COLORS"))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(350, 0)

    def move_car(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

        if car_manager.xcor() < -320:
            car_manager.reset()


    def increase_speed(self):
        new_x = STARTING_MOVE_DISTANCE - MOVE_INCREMENT