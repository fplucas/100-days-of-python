from turtle import Turtle
STARTING_MOVE_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = STARTING_MOVE_SPEED

    def move(self, paddles):
        if self.hit_the_wall():
            self.bounce('y')
        for paddle in paddles:
            if self.hit_the_paddle(paddle):
                self.bounce('x')
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def hit_the_wall(self):
        return self.ycor() > 280 or self.ycor() < -280

    def hit_the_paddle(self, paddle):
        return self.distance(paddle) < 50 and (self.xcor() > 320 or self.xcor() < - 320)

    def reset_position(self):
        self.move_speed = STARTING_MOVE_SPEED
        self.goto(0, 0)
        self.bounce('x')

    def bounce(self, axis):
        if axis == 'x':
            self.x_move *= -1
        elif axis == 'y':
            self.y_move *= -1
        self.move_speed *= 0.9
