from random import choice, randint
from turtle import Turtle, Screen

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
STARTING_X = -230
STARTING_Y = -120

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet',
                            prompt='Which turtle will win the race? Enter a color: ')


def create_turtle(color):
    turtle = Turtle('turtle')
    turtle.color(color)
    return turtle


shift = 0
turtles = []
for color in COLORS:
    turtle = create_turtle(color)
    turtle.penup()
    turtle.goto(STARTING_X, STARTING_Y + shift)
    shift += 50
    turtles.append(turtle)

is_race_on = True
while is_race_on:
    for turtle in turtles:
        distance = randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() > 220:
            is_race_on = False
            winner = turtle.color()

print(f"The winner was {winner[0]}.")
if winner == user_bet:
    print("You won!")
else:
    print("You lost!")

screen.exitonclick()
