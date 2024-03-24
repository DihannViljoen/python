import turtle
corners = int(input ("num of corners? "))
turtle.speed("fastest")
s = turtle.getscreen()
t = turtle.Turtle()
for i in range(corners):
    t.right(360/corners)
    t.forward(50)

turtle.Screen().exitonclick()    