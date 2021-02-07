"""
100 days of Python course
DAY 18
"""

from turtle import Turtle, Screen

# naming the turtle
# timmy_the_turtle = Turtle()
# from here onwards, use convention t = Turtle()

# examples giving it shape, color and demonstrating
# movement (forward) and turning right (angle)
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("CornflowerBlue")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# abbreviations: forward = fd, right = rt

t = Turtle()
t.shape("arrow")
t.color("black")

# challenge no. 1 - draw a square
def square():
    """draw a square with sides 200"""
    for _ in range(4):
        t.fd(200)
        t.rt(90)

square()

# these lines need to be at the end of the program
screen = Screen()
screen.exitonclick()
