"""
100 days of Python course
DAY 18
"""

# note we are using a different import here
import turtle as t
import random

## challenge no. 4 - random walk: using colormode to randomise the changing
## colours: note the way of calling this function/special method whigh
## is reflected in the way we import turtle

## here the turtle will walk 15 paces in a random direction which is the
## equivalent to north, south, west, east etc. The trail is also bigger
## so that we can see the output better
tim = t.Turtle()
t.colormode(255)


def random_color():
    """use rgb values 0 - 255 randomly"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# these lines need to be at the end of the program
screen = Screen()
screen.exitonclick()
