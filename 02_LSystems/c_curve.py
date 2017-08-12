import turtle
from math import sqrt, pi, cos, sin
import sys


sys.setExecutionLimit(60 * 1000)


def plot(vec_seq, scale=1):
    """Draw the given sequences of points with a turtle"""
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    t.hideturtle()
    t.goto(scale * vec_seq[0][0], scale * vec_seq[0][1])
    t.pendown()

    for vec in vec_seq[1:]:
        t.goto(scale * vec[0], scale * vec[1])


def levy(x, y, length, angle, it):
    if it:
        length = length / sqrt(2)
        left = levy(x, y, length, angle + pi/4, it - 1)
        x = x + length * cos(angle + pi/4)
        y = y + length * sin(angle + pi/4)
        right = levy(x, y, length, angle - pi/4, it - 1)
        return left + right
    else:
        return [(x, y), (x + length * cos(angle), y + length * sin(angle))]


plot(levy(0, -50, 100, pi/2, 10))
