from turtle import Turtle


class CreateTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        self.y_move = 25

    def move_up(self):
        self.forward(10)
