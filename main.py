import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.bgcolor("snow2")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing!")

screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_back, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    # car_manager.move_car()
    car_manager.create_car()
    car_manager.move_cars()

    # Player successfully crossed
    if player.ycor() > 250:
        player.scored()
        car_manager.level_up()
        scoreboard.clear()
        scoreboard.safely_across()
        # car_manager.player_scored()

    # Player got hit/game over
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
