from turtlr import *

bgcolor("black")
speed(0)

for i in range(7):
    for color in ('red','cyan','white','magenta','yellow','purple'):
        color(color)
        circle(100)
        right(10)
        
hideturtle()
