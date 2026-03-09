 # Write a program to draw a star using a turtle?
import turtle

turtle.Screen().bgcolor("white")
board=turtle.Turtle()

# 1st triangle for star
board.forward(100)
board.left(120)
board.forward(100)
board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)
board.pendown()

# second triangle for star
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

turtle.done()