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


# tim.shape("turtle")
# random_color = random.choice(Colors)
# tim.color(random_color)
# for i in range(20):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# tim.up()
# tim.backward(100)
# tim.left(90)
# tim.up()
# tim.forward(345)
# tim.right(90)
# tim.forward(100)
# tim.down()

# def draw_shape(num):
#     angle = 360/num
#     random_color = random.choice(Colors)
#     tim.color(random_color)
#     for i in range(num):
#         tim.right(angle)
#         tim.forward(50)

# for j in range(3,45):
#     draw_shape(j)

# for i in range(3, 10):
#     random_color = random.choice(Colors)
#     tim.color(random_color)
#     for j in range(i):
#         angle = 360/i
#         tim.right(angle)
#         tim.forward(50)

# direction = [0, 90, 180, 270]
# tim.pensize(10)
# tim.speed(100)
# turtle.colormode(255)
# def random_colors():
#     r = int(random.randint(0, 255))
#     g = int(random.randint(0, 255))
#     b = int(random.randint(0, 255))
#     random_color = (r, g, b)
#     return random_color
#
# for i in range(200):
#     # random_color = random.choice(Colors)
#     tim.color(random_colors())
#     tim.forward(30)
#     tim.setheading(random.choice(direction))

my_screen = Screen()
my_screen.delay(100)
my_screen.exitonclick()
