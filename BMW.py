import turtle
import math

def draw_digital_bmw():

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("#050505")
    screen.title("Digital BMW")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    COLORS = {
        "blue": "#0066AD",
        "white": "#FFFFFF",
        "chrome": "#E0E0E0",
        "grid": "#222222"
    }

    # Draw outer circles
    for radius in range(250, 220, -5):
        t.penup()
        t.goto(0, -radius)
        t.setheading(0)
        t.pendown()
        t.pencolor(COLORS["chrome"])
        t.circle(radius)

    # Draw inner circle
    t.penup()
    t.goto(0, -190)
    t.setheading(0)
    t.pendown()
    t.pencolor(COLORS["white"])
    t.circle(190)

    # Draw four sections
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()

    for angle in [0, 90, 180, 270]:
        t.setheading(angle)
        t.forward(190)
        t.backward(190)

    # Color the four sections
    t.penup()
    t.goto(0, 0)

    t.goto(0, 0)
    t.fillcolor(COLORS["blue"])
    t.begin_fill()

    for _ in range(2):
        t.forward(190)
        t.left(90)

    t.end_fill()

    # Center circle
    t.penup()
    t.goto(0, -45)
    t.setheading(0)
    t.pendown()
    t.pencolor(COLORS["chrome"])
    t.circle(45)

    screen.update()
    turtle.done()


draw_digital_bmw()