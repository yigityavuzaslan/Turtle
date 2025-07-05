import turtle

turtle_screem = turtle.Screen()
turtle_screem.bgcolor("white")
turtle_screem.title("Square Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("red")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size=size-5
        turtle_instance.speed(10)

shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(70)
shrinkingSquare(50)
shrinkingSquare(30)
turtle.done()