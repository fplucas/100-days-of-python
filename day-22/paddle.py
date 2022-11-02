from turtle import Turtle
SPEED = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + SPEED)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - SPEED)
