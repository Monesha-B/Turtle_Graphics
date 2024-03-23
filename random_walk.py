import random
import turtle
from turtle import Turtle, Screen
from colors import Colors

tim = Turtle()
direction = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(100)
turtle.colormode(255)
def random_colors():
    r = int(random.randint(0, 255))
    g = int(random.randint(0, 255))
    b = int(random.randint(0, 255))
    random_color = (r, g, b)
    return random_color

for i in range(200):
    # random_color = random.choice(Colors)
    tim.color(random_colors())
    tim.forward(30)
    tim.setheading(random.choice(direction))

my_screen = Screen()
my_screen.delay(100)
my_screen.exitonclick()