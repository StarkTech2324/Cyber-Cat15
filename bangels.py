import turtle

turtle.bgcolor("black")
turtle.speed(0)

for i in range(8):
    for color in ('red','cyan','white','magenta','yellow'):
        turtle.color(color)
        turtle.circle(100)
        turtle.right(10)
        
turtle.hideturtle()
