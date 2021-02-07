"""
100 days of Python course
DAY 18
"""

from turtle import Turtle, Screen
import random


t = Turtle()
t.shape("arrow")
t.color("black")

# challenge no. 3 - draw a triangle, square, pentagon, hexagon,
# heptagon, octagon, nonagon and decagon i.e. 3 sides, 4 sides etc
# up to 10 sides. Length of each side is 100
# use concept that angles are e.g. triangle 360 / 3 = 120 deg
# change pen colour randomly for each shape

LENGTH = 100

def colours():
    """choose a random color from provided pallette"""
    random_colors  = ["red","green","blue","orange","purple","pink","yellow","brown","indigo"]
    my_color = random.choice(random_colors)
    return my_color

def shapes(sides):
    """draw the various shapes returning to start position"""
    angle = 360 / sides
    for _ in range(sides):
        t.fd(LENGTH)
        t.rt(angle)

for i in range(3, 11):
    t.color(colours())
    shapes(i)

# these lines need to be at the end of the program
screen = Screen()
screen.exitonclick()
