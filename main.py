import turtle
##ekran
drawing_board = turtle.Screen()
drawing_board.bgcolor("Light Blue")
drawing_board.title("Python Turtle")

##cizim
'''
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
'''
##square
turtle_instance2 =turtle.Turtle()
'''
for i in range(4):
    turtle_instance2.forward(250)
    turtle_instance2.right(90)

turtle.done()
'''

'''
turtle_instance2.left(90)
turtle_instance2.forward(100)
turtle_instance2.right(90)
turtle_instance2.forward(100)
turtle_instance2.right(90)
turtle_instance2.forward(100)
turtle_instance2.right(90)
turtle_instance2.forward(100)

turtle.done()
'''

##star
'''
turtle_instance3=turtle.Turtle()
for i in range(5):
    turtle_instance3.forward(300)
    turtle_instance3.right(144)


turtle_instance3.forward(100)
turtle_instance3.right(144)
turtle_instance3.forward(100)
turtle_instance3.right(144)
turtle_instance3.forward(100)
turtle_instance3.right(144)
turtle_instance3.forward(100)
turtle_instance3.right(144)
turtle_instance3.forward(100)
turtle_instance3.right(144)
turtle.done()
'''

'''
##polygon
turtle_instance4 = turtle.Turtle()
num_sides = 10
angle =360.0/num_sides
side_length =100

for i in range(num_sides):
    turtle_instance4.right(angle)
    turtle_instance4.forward(side_length)

turtle.done()
'''

