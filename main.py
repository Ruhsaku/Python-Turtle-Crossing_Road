from turtle import Screen
from myturtle import CreateTurtle

# Create and modify the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing the Road")
screen.tracer(0)

# Create objects
timmy = CreateTurtle()

# Variables
game_is_on = True

screen.listen()
screen.onkey(fun=timmy.move, key="Up")

while game_is_on:
    screen.update()

screen.exitonclick()
