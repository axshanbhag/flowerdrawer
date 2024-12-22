import turtle as trtl
import random

painter = trtl.Turtle()
painter.speed(0)

def flower(color, x, y):
    painter.penup()
    painter.goto(x,y)
    painter.pendown()
    for i in range(82):
        painter.pencolor(color)  
        painter.forward(i)
        painter.right(55)
    painter.penup()
    painter.goto(x,y)
    painter.pendown()
    painter.setheading(270)
    painter.pencolor("green")
    painter.forward(300)

colors = ["red", "orange", "yellow", "blue", "purple", "#FF00FF"]
while True:
    width = input("Enter screen width in pixels: ")
    if width.isdigit():
        width = int(width)
        break
    else:
        print("Invalid input. Please enter a valid integer.")
while True:
    height = input("Enter screen height in pixels: ")
    if height.isdigit():
        height = int(height)
        break
    else:
        print("Invalid input. Please enter a valid integer.")

screen = trtl.Screen()
screen.setup(width = width, height = height)
screen.bgcolor("#ADD8E6")

for i in range(20):
    xcod = random.randint((-1 * width), width)
    ycod = random.randint((-1 * height), height)
    color = colors[i%6]
    flower(color, xcod, ycod)

wn = trtl.Screen()
wn.mainloop()
