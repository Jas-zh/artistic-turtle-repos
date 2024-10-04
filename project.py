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

def semicircle():
    t.pencolor(0.871, 0.859, 0.345)
    t.fillcolor(0.941, 0.922, 0.176)
    t.begin_fill()
    t.right(180)
    t.forward(175)
    t.left(90)
    t.circle(150, extent= 180)
    t.left(90)
    t.forward(175)
    t.end_fill()
    


ground()
semicircle()
ground()



sc.update()
sc.exitonclick()
