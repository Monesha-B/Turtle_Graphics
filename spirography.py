import random
import turtle
from turtle import Turtle, Screen
from colors import Colors

tim = Turtle()



direction = [0, 90, 180, 270]

tim.speed(100)
turtle.colormode(255)

def random_colors():
    r = int(random.randint(0, 255))
    g = int(random.randint(0, 255))
    b = int(random.randint(0, 255))
    random_color = (r, g, b)
    return random_color


# tim.speed("fastest")
def cir(gapsize):
    c= int(360 / gapsize)
    for i in range(c):
        tim.speed(100)
        tim.color(random_colors())
        tim.circle(170)
        tim.setheading(tim.heading()+gapsize)


cir(0.5)


my_screen = Screen()
my_screen.delay(100)
my_screen.exitonclick()