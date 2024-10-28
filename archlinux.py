# Set up
import turtle
import random
import time

t = turtle.Turtle()
sc = turtle.Screen()

sc.bgcolor("black")
sc.tracer(20)

t.left(180)

#Setup
t.penup()
t.forward(150)
t.right(110)

#Frame code i stole
def frame():
    t.pencolor("blue")
    t.up()
    t.goto(350, -350)   
    t.pensize(10)
    t.down()
    t.goto(350, 350)    
    t.goto(-350, 350)   
    t.goto(-350, -350)  
    t.goto(350, -350)

# Cool Sqaure spiral
def squaredows():
   t.pendown()
   t.fillcolor(random.randint(0,1),random.randint(0,1),random.randint(0,1))
   t.pencolor(random.randint(0,1),random.randint(0,1),random.randint(0,1))
   t.circle(55, steps=4)

#Cool square spiral cont.
def squarespiral():
    t.penup()
    t.goto(random.randint(-300,300),random.randint(-300,300))
    t.pendown()
    for i in range(3):
        squaredows()
        t.forward(25)
    
#Geometric Logo of Arch Linux
def archlinux():
    t.pendown()
    t.fillcolor("#4592cc")
    t.pencolor("#4592cc")
    t.pensize(15)
    t.pendown()
    t.forward(250)
    t.right(135)
    t.forward(250)
    t.right(145)
    t.forward(75)
    t.right(59)
    t.forward(25)
    t.circle(20 , extent=180)
    t.forward(25)
    t.right(60)
    t.forward(105)
    t.penup()

# Cool shapes
def randeverything():
    for i in range(1):
        t.begin_fill()
        t.penup()
        t.pencolor(random.random(), random.random(), random.random())
        t.fillcolor(random.random(), random.random(), random.random())
        t.goto(random.randint(-300,300), random.randint(-300,300))
        t.pendown()
        t.circle(radius= 80, steps= random.randint(3,10))
        t.end_fill()
        

#Animation code
a=0
while a < 1:
    a = 0
    sc.tracer(20)
    sc.bgcolor("black")
    frame()
    for i in range(6):
        t.pendown()
        archlinux()
        t.penup()
        t.goto(random.randint(-200,200),random.randint(-200,200))
    for i in range(5):
        squarespiral()
    for i in range(7):
        t.pencolor(random.randint(0,1),random.randint(0,1),random.randint(0,1))
        t.pendown()
        t.write("Jason", font=("Trebuchet MS bold", 50))
        randeverything()
        t.penup()
        t.goto(random.randint(-300,300),random.randint(-300,300))
    frame()
    time.sleep(1)
    sc.update()
    sc.clear()
