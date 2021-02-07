"""
100 days of Python course
DAY 18
"""

# note we are using a different import here
import turtle as t
import random

## challenge no. 5 - Spirograph: each circle has a radius of 100 in distance
## resulting in what looks like a donut with a pinprick hole:)

# re-using snippets from previous exercise
tim = t.Turtle()
t.colormode(255)


def random_color():
    """use rgb values 0 - 255 randomly"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


tim.pensize(3)
tim.speed("fastest")

for _ in range(72):
    tim.color(random_color())
    tim.circle(100)
    tim.left(5)
    

# these lines need to be at the end of the program
screen = t.Screen()
screen.exitonclick()

## notes from course: alternate code:
# tim.speed("fastest")

# def draw_spiro(gapsize):
#     for _ in range(int(360 / gapsize)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.seth(tim.heading() + gapsize)
        
# draw_spiro(5)