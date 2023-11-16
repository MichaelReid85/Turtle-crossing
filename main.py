import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# TODO - Get turtle to cross
# TODO - Keep score
# TODO - Make cars cross randomly


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing!")

screen.listen()
screen.onkeypress(player.move_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_car()

    if player.ycor() > 250:
        player.scored()
        scoreboard.clear()
        scoreboard.safely_across()
        car_manager.increase_speed()






screen.exitonclick()