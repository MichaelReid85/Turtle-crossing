from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 7)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(350, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    # def __init__(self):
    #     super().__init__()
    #     self.shape("square")
    #     self.penup()
    #     self.color(random.choice(COLORS))
    #     random_y = random.randint(-250, 250)
    #     self.shapesize(stretch_wid=1, stretch_len=2)
    #     self.goto(350, random_y)
    #     self.move_speed = STARTING_MOVE_DISTANCE
    #
    # def move_car(self):
    #     new_x = self.xcor() - self.move_speed
    #     self.goto(new_x, self.ycor())
    #
    #     if self.xcor() < -320:
    #         self.reset()
    #         self.penup()
    #         self.color(random.choice(COLORS))
    #         self.shapesize(stretch_wid=1, stretch_len=2)
    #         random_y = random.randint(-250, 250)
    #         self.goto(350, random_y)
    #
    # def player_scored(self):
    #     self.reset()
    #     self.penup()
    #     self.color(random.choice(COLORS))
    #     self.shapesize(stretch_wid=1, stretch_len=2)
    #     self.goto(350, 0)
    #     self.move_speed += MOVE_INCREMENT


