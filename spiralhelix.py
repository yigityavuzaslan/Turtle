import turtle

turtle_screen=turtle.Screen()
turtle_screen.bgcolor("White")
turtle_screen.title("Python Turtle")

turtle_instance=turtle.Turtle()
turtle_instance.color("orange")

turtle_colors=["red","yellow","green","blue","purple"]

for i in range(100):
    turtle_instance.color(turtle_colors[i % 5])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)
    turtle_instance.speed(0)
turtle.done()