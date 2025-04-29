import turtle as t
import random
from math import sqrt


t = t.Turtle()# Initialize the turtle

def tri_curve(depth, dist):
    if depth == 0:# Base case: stop recursion when depth is 0
        t.forward(dist)
    else:# Move turtle to initial drawing position
        t.reset()
        t.right(90)
        t.penup()
        t.forward(240)
        t.left(90)
        t.pendown()
        t.left(90)
        t.forward(240)
        t.right(135)
        t.forward(340)
        t.left(45)
        t.forward(140)

# Recursive function to draw the dragon curve
def tri_curve(depth, dist,color,width):
    if depth == 0:# Base case: stop recursion when depth is 0
        t.forward(dist)# Draw a line segment of specified distance
    else:
        t.color(color)
        t.width(width)
        tri_curve(depth - 1, dist * 0.5, color, width)  # Recursive call 1 with reduced depth and distance
        t.right(130)
        tri_curve(depth - 1, dist * 0.5, color, width)  # Recursive call 2 with reduced depth and distance
        t.left(40)
        tri_curve(depth - 1, dist * 0.5, color, width)
        t.right(80)  # Recursive call 3 with reduced depth and distance

# Recursive function to draw the dragon curve backwards
def tri_curve_reverse(depth, dist, color, width):
    if depth == 0:# Base case: stop recursion when depth is 0
        t.forward(dist)
    else:
        t.color(color)
        t.width(width)
        tri_curve_reverse(depth - 1, dist * 0.5, color, width)  # Recursive call 1 with reduced depth and distance
        t.left(130)
        tri_curve_reverse(depth - 1, dist * 0.5, color, width)  # Recursive call 2 with reduced depth and distance
        t.right(40)
        tri_curve_reverse(depth - 1, dist * 0.5, color, width)  # Recursive call 3 with reduced depth and distance
        t.left(80)

# Set up initial drawing position
t.reset()
t.right(90)
t.width(0.5)
t.pendown()

# Draw the curve with recursion
t.speed('fastest')
tri_curve(2, 400, "blue", 2)

# Draw the curve backwards
t.penup()
t.goto(0, 0)  # Reset turtle position
t.pendown()
t.left(90)
t.width(0.5)
t.speed('fastest')
tri_curve_reverse(8, 4000, "red", 3)
