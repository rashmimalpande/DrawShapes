import turtle


def draw_square(some_turtle):
    count = 0
    while (count <= 3):
        some_turtle.forward(100)
        some_turtle.right(90)
        count += 1


def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    turt = turtle.Turtle()
    turt.shape("turtle")
    draw_square(turt)
    # draw a circle
    angie = turtle.Turtle()
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()


draw_art()
