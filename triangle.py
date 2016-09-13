import turtle


def draw_triangle(some_turtle):
    for i in range(1, 4):
        some_turtle.forward(100)
        some_turtle.left(60)
        some_turtle.left(60)


def flower():
    window = turtle.Screen()
    window.bgcolor("blue")

    turt = turtle.Turtle()
    turt.shape("turtle")

    for i in range(1, 37):
        draw_triangle(turt)
        turt.right(10)

    window.exitonclick()


flower()
