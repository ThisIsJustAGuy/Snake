import turtle
import time


def balra():
    fej.left(90)


def jobbra():
    fej.right(90)


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)  # animáció sebessége
palya.listen()

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("black")

palya.onkey(balra, "Left")
palya.onkey(jobbra, "Right")

while True:
    fej.forward(20)
    palya.update()
    time.sleep(0.25)
