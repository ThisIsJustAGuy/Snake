import turtle
from time import sleep
from random import randint


def balra():
    fej.left(90)


def jobbra():
    fej.right(90)


def gyumolcs_kirak():
    x = randint(-380, 380)
    y = randint(-280, 280)
    gyumolcs.goto(x, y)


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

kijelzo = turtle.Turtle()
kijelzo.color("white")
kijelzo.hideturtle()
kijelzo.clear()

gyumolcs_kijelzo = turtle.Turtle()
gyumolcs_kijelzo.color("white")
gyumolcs_kijelzo.hideturtle()
gyumolcs_kijelzo.clear()
gyumolcs_kijelzo.penup()
gyumolcs_kijelzo.goto(0, -280)
gyumolcs_kijelzo.write("0", font=("Fira Code Retina", 12, "bold"), align="center")

gyumolcs = turtle.Turtle()
gyumolcs.penup()
gyumolcs.color("red")
gyumolcs.shape("circle")

darab_gyumolcs = 0
gyumolcs_kirak()

while True:
    fej.forward(20)
    if fej.distance(gyumolcs.xcor(), gyumolcs.ycor()) <= 15:
        gyumolcs_kirak()
        darab_gyumolcs += 1
        gyumolcs_kijelzo.clear()
        gyumolcs_kijelzo.write("{}".format(darab_gyumolcs), font=("Fira Code Retina", 12, "bold"), align="center")
    if not (-290 <= fej.ycor() <= 290) or not (-380 <= fej.xcor() <= 380):
        kijelzo.clear()
    palya.update()
    sleep(0.25)
