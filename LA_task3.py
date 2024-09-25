import turtle
import random

t = turtle.Turtle()
sc = turtle.Screen()
sc.bgcolor('RoyalBlue3')
sc.setup(600,600)
sc.tracer(20)

t.pensize(10)
t.fillcolor("silver")
t.pencolor("blue")

def square():
    t.pendown()
    t.begin_fill()
    for x in range (4):
        t.forward(100)
        t.right(90);
    t.end_fill()
    t.penup()

def antisquare():
    t.pendown()
    t.begin_fill()
    for x in range (4):
        t.forward(100)
        t.left(90)
    t.end_fill()
    t.penup()
    
def spiral():
    t.pendown();
    t.pencolor("black")
    width = 1
    dist = 10
    for i in range (50):
        t.pensize(width)
        t.forward(dist)
        t.left(90)
        dist += 10
        width = random.randint(0,5)
def anotherspiral():
    dist2 = 0.01
    width2 = 0.1
    colorpicker = random.randint(0,2)
    if colorpicker == 0:
        colour = "blue4"
    elif colorpicker == 1:
        colour = "gold"
    else:
        colour = "black"
     
    for i in range (1000):
        if colorpicker == 0:
            colour = "blue4"
        elif colorpicker == 1:
            colour = "gold"
        else:
            colour = "black"
        t.forward(dist2)
        t.pensize(width2)
        t.pencolor(colour)
        t.right(1)
        dist2 += 0.01
        width2 += 0.1
def snowflakes():
    t.home()
    t.pencolor("white")
    t.pensize(19)
    for i in range (15):
        t.pendown()
        t.circle(10)
        t.penup()
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        t.goto(x,y)

    
def starwithpent():
    t.pensize(10)
    t.fillcolor("yellow")
    t.pencolor("grey")
    t.home()
    t.begin_fill()
    for i in range (5):
        t.forward(100)
        t.left(72)
    t.end_fill()
    
def penupdown():
    t.penup()
    t.home()
    t.pendown()
    

square()
t.forward(150)
t.fillcolor("orange")
t.pencolor("green")
square()
t.right(90)
t.forward(150)
t.left(90)
t.fillcolor("gold")
t.pencolor("red")
square()
t.left(180)
t.forward(50)
t.fillcolor("purple")
t.pencolor("orange")
antisquare()

spiral()

penupdown()

anotherspiral()
penupdown()
snowflakes()
penupdown()
starwithpent()



