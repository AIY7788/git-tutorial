import turtle
import math
import random


screen = turtle.Screen()
screen.bgcolor("yellow")
screen.title("color unique animation")

t = turtle.Turtle()
t.speed(-1)
t.width(2)
t.hideturtle()

color = ["red", "blue", "green"]

for i in range(300):
    t.color(random.choice(color))
    t.forward(i * 3)
    t.right(250)