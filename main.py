from turtle import Screen
from myturtle import CreateTurtle
from car import Car
import time

# Create and modify the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing the Road")
screen.tracer(0)

# Create objects
player = CreateTurtle()
car_manager = Car()

# Variables
game_is_on = True

# Create a movement
screen.listen()
screen.onkey(fun=player.move_up, key="Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()


screen.exitonclick()
