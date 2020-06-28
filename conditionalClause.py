# This code draws three yellow flowers.
# Change it so the third flower is green.
# You don't need to change the 'petal' or
# 'flower' functions.

import turtle

def flower(tur):
    # This flower has 12 petals.
    for p in range(12):
        petal(tur)
 
def petal(tle):
    # Draw a long narrow petal.
    tle.forward(36)
    tle.right(60)
    tle.forward(12)
    tle.right(90)
    tle.forward(12)
    tle.right(60)
    tle.forward(36)

mellie = turtle.Turtle()
mellie.speed(0)
mellie.width(2)
mellie.penup()
mellie.back(100)
mellie.pendown()

mellie.color("red")
for bloom in range(3):
    if bloom == 2:
        mellie.color("blue")
    if bloom == 1:
        mellie.color("yellow")
    flower(mellie)
    mellie.penup()
    mellie.forward(100)
    mellie.pendown()
