import turtle

t = turtle.Turtle()
sc = turtle.Screen()

sc.tracer(1)
t.right(90)
t.penup()
t.forward(200)
t.pendown()

def ground():
    t.pencolor(0.306, 0.412, 0.294)
    t.pensize(15)
    t.fillcolor(0.369, 0.459, 0.357)
    t.begin_fill()
    t.right(90)
    for i in range(4):
        t.forward(350)
        t.right(-90)
        t.forward(350)
    t.end_fill()

ground()





sc.update()
sc.exitonclick()
