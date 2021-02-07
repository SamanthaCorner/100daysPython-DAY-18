"""
100 days of Python course
DAY 18
"""

from turtle import Turtle, Screen

t = Turtle()
t.shape("arrow")
t.color("black")

# challenge no. 2 - draw a dashed line consisting of 10 solid moves and
# 10 blank moves which is repeated 50 times
# new abbreviations penup(pu) which doesn't draw and pendown(pd)
def dashed():
    """draw dashed lines of 10 by 10 (solid by space)"""
    for _ in range(15):
        t.pd()
        t.fd(10)
        t.pu()
        t.fd(10)

dashed()

# these lines need to be at the end of the program
screen = Screen()
screen.exitonclick()
