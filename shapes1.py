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

def draw_shape(num):
    angle = 360/num
    random_color = random.choice(Colors)
    tim.color(random_color)
    for i in range(num):
        tim.right(angle)
        tim.forward(50)

for j in range(3,45):
    draw_shape(j)