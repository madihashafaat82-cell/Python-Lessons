import turtle
turtle.Screen().bgcolor('Dark blue')
sc = turtle.Screen()
sc.setup(400,400)
turtle.title("Welcome to my Window")
board = turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.left(90)
    i = i+1