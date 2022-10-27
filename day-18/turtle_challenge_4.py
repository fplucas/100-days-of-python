import random
import turtle as t


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim = t.Turtle('turtle')
t.colormode(255)
tim.speed('fastest')
tim.pensize(20)

for _ in range(200):
    tim.color(random_color())
    tim.right(random.randint(0, 4) * 90)
    tim.forward(30)
