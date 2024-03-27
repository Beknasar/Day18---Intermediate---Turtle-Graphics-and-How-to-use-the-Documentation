# # random walk turtle
# # from turtle import Turtle, Screen
# import turtle as t
# import random
# # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
# #            "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_clr = (r, g, b)
#     return random_clr
#
#
# tim = t.Turtle()
# t.colormode(255)
#
# tim.pensize(15)
# tim.speed(10)
# directions = [0, 90, 180, 270]
#

# for _ in range(400):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))


# Spirograph
import turtle as t
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
# My solution
# for angle in range(0, 361, 5):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(angle)


# Dr.Angela's solution
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(3)
screen = t.Screen()
screen.exitonclick()
