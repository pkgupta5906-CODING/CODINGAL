# Write a program to set screen size, colour for turtle graphics and draw a polygon using turtle?
import turtle # importing turtle library

turtle.Screen().bgcolor("blue")
turtle.Screen().setup(300,300)
n=int(input("Enter number of sides : "))
angle=360/n
sideLength=70
turtle.speed(1)
turtle.pensize(2) # To incraese thickness of line .
polygon=turtle.Turtle()
for i in range(n):
    polygon.forward(sideLength)
    polygon.right(angle)

    
turtle.done()
 