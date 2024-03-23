import random
import turtle
from turtle import Turtle, Screen
from colors import Colors

tim = Turtle()
tim.up()
tim.backward(100)
tim.left(90)
tim.up()
tim.forward(345)
tim.right(90)
tim.forward(100)
tim.down()

for i in range(3, 45):
    random_color = random.choice(Colors)
    tim.color(random_color)
    for j in range(i):
        angle = 360/i
        tim.right(angle)
        tim.forward(50)