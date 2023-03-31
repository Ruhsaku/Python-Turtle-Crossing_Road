from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard
import time

# Create and modify the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing the Road")
screen.tracer(0)

# Create objects
player = Player()
car_manager = Car()
scoreboard = Scoreboard()

# Variables
game_is_on = True
car_player_dist = 22

# Create a movement
screen.listen()
screen.onkey(fun=player.move_up, key="Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < car_player_dist:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.level_up()


screen.exitonclick()
