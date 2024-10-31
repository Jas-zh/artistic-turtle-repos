import turtle
import random

t = turtle.Turtle()
sc = turtle.Screen()

sc.bgcolor('LightSkyBlue')
sc.tracer(0)
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

def randeverything():
    for i in range(10):
        t.begin_fill()
        t.penup()
        t.pencolor(random.random(), random.random(), random.random())
        t.fillcolor(random.random(), random.random(), random.random())
        t.goto(random.randint(-300,300), random.randint(-300,300))
        t.pendown()
        t.circle(radius= 80, steps= random.randint(3,10))
        t.end_fill()
        


ground()
semicircle()
randeverything()

#Floating Island
t.penup()
t.goto(0,100)
t.pencolor("#32a0a8")
t.fillcolor("#32a88f")
t.pensize(25)
t.pendown()
t.begin_fill()
t.circle(radius=400, steps=5)
t.end_fill()

#Waterfall
t.penup()
t.pencolor("#3792b3")
t.fillcolor("#3792b3")
for i in range(5):
    t.begin_fill()
    t.goto(random.randint(-250, 250), random.randint(200,300))
    t.pendown()
    t.circle(radius=60, steps=4)
    t.penup()
    t.end_fill()

#Frame
t.up()
t.goto(400, -400) 
t.down()
t.goto(400, 400)    # Top right
t.goto(-400, 400)   # Top left
t.goto(-400, -400)  # Bottom left
t.goto(400, -400)
t.penup()

#Signature
t.goto(130,-320)
t.pendown()
t.pencolor("#333c42")
t.write("Jason", font=("noto_sans", 69))

sc.update()
sc.exitonclick()
