import turtle

def move():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

    
def down():
    turtle.stamp()
    turtle.setheading(-90)
    turtle.forward(50)

def turn_left():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def turn_right():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def restart():
    turtle.reset()


turtle.shape('turtle')

turtle.onkey(move, 'w')
turtle.onkey(down,'s')
turtle.onkey(turn_left, 'a')
turtle.onkey(turn_right, 'd')
turtle.onkey(restart,'Escape')
turtle.listen()
