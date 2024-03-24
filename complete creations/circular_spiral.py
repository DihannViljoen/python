import turtle
turtle.bgcolor("green")
s = turtle.getscreen()
t = turtle.Turtle()
t.penup()
t.goto(0,0)
t.pensize(3)
t.speed(0)
t.pendown()
for i in range(120):
    t.fd(1*i)
    t.lt(50-i*(1/2))





turtle.Screen().exitonclick()    