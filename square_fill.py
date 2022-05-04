import turtle

t=turtle.Turtle()
t.forward(100)

#t.backward(300)
t.begin_fill()
t.fillcolor("red")
for i in range(3):
    t.left(90)
    t.forward(100)
t.hideturtle()
t.end_fill()
turtle.done()