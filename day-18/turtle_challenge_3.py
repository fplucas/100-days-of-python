import random
import turtle as t

COLORS = ['black', 'blue', 'red', 'yellow', 'purple']


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


tim = t.Turtle('turtle')

for sides in range(3, 11):
    tim.pencolor(random.choice(COLORS))
    draw_shape(sides)
