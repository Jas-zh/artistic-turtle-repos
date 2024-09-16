import turtle

t = turtle.Turtle()
sc = turtle.Screen
i = 0

def tright():
    t.forward(100)
    t.right(135)

t.left(90)
tright()

t.forward(100)
t.right(45)
tright()
 
i = 0
while i < 2:
 t.forward(100)
 t.right(45)
 i+=1

t.right(45)
t.forward(150)
t.right(135)

t.forward(100)

sc.update