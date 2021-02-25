import turtle
import time

palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)  # animáció sebessége
palya.listen()

while True:
    palya.update()
    time.sleep(0.3)
