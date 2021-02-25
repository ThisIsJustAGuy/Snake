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

kijelzo = turtle.Turtle()
kijelzo.color("white")
kijelzo.hideturtle()
kijelzo.clear()

el = True

while el:
    fej.forward(20)
    palya.update()
    if not (-290 <= fej.ycor() <= 290) or not (-380 <= fej.xcor() <= 380):
        kijelzo.write("A kukac meghalt", font=("Fira Code Retina", 16, "bold"), align="center")
        el = False
    time.sleep(0.25)
