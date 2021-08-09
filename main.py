from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Initialize player, car manager, and scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")

# Main game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    # Detect player crossing finish line
    if player.is_at_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.level_up()


screen.exitonclick()
