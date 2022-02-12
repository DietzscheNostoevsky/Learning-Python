# Use for loops to make a turtle draw these regular polygons (regular means all sides the same lengths, all angles the same):
# An equilateral triangle
# A square
# A hexagon(six sides)
# An octagon(eight sides)

import turtle

# Creating a general purpose code whcih asks user to enter
# number of side in the regular polygon and creates a polygon of that side

wn = turtle.Screen()
kachua = turtle.Turtle()

side = int(input("Enter the number of sides in the polygon :"))

angle = 360/side  # calculates the angle turtle have to turn

for i in range(side):
    kachua.forward(100)
    kachua.left(angle)
wn.exitonclick()
