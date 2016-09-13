import turtle


def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    turt = turtle.Turtle()
    turt.shape("turtle")
    turt.forward(100)
    turt.right(90)
    turt.forward(100)
    turt.right(90)
    turt.forward(100)
    turt.right(90)
    turt.forward(100)
    turt.right(90)
    window.exitonclick()


draw_square()
