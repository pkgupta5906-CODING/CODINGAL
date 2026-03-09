# Write a program to draw a square inside a square?
import turtle

spiralBoard=turtle.Screen()
spiralBoard.bgcolor("white")
spiralBoard.title("Spiral Pattern")
spiralPen=turtle.Turtle()
size=0

# while size>=-100:
while True:
    for i in range(4):
        spiralPen.fd(size+1)
        spiralPen.left(90)
        size=size-5
    size=size+1
turtle.Turtle.done()