# Get a colours with colorgram
# import colorgram

#

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r, g, b = color.rgb
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as turtle_module

tom = turtle_module.Turtle()
tom.speed("fastest")
tom.hideturtle()
tom.pu()
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136),
              (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
              (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50),
              (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
              (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64),
              (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def draw_dot_raw(pos_y):
    for _ in reversed(range(10)):
        tom.setx(x)
        pos_y += 50
        tom.sety(pos_y)
        for _ in range(10):
            tom.dot(20, random.choice(color_list))
            tom.forward(50)


turtle_module.colormode(255)
y = -300
x = -225
draw_dot_raw(y)
screen = turtle_module.Screen()
screen.exitonclick()
