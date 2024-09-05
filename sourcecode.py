# Generalities
import turtle

t = turtle.Turtle()
sc = turtle.Screen
i = 0

#CSS
t.pensize(30)
t.pencolor("gold2")
t.fillcolor("yellow2")

# Picasso's dream
t.begin_fill()
while i < 6:
 t.forward(100)
 t.left(60)
 i += 1

t.forward(100)
i = 0

while i < 6:
    t.right(60)
    t.forward(100)
    i += 1

t.left(60)
i = 0
while i < 6:
 t.forward(100)
 t.right(60)
 i += 1

t.forward(100)
t.left(60)
i=0

while i < 6:
 t.forward(100)
 t.right(60)
 i += 1 

t.end_fill()

t.penup()
t.forward(200)
t.left(90)
t.forward(300)

#BEE CSS
t.pencolor("black")
t.pensize(15)
t.fillcolor("gold2")
#BEEEEEEEE
t.begin_fill()
t.pendown()
r = 75
t.circle(r)

t.penup()
t.forward(100)
t.pendown()
t.circle(r-10)
t.end_fill()

t.left(90)
t.forward(100)

#Outro
sc.update()
sc.exitonclick()	
