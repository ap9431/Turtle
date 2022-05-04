import turtle
wc =turtle.Screen()
t=turtle.Turtle()
def fxn(x,y):
    turtle.forward(300)
    #turtle.backward(500)
#wc.onclick(fxn)
turtle.width(20)
turtle.color("red")
turtle.bgcolor("black")

t.up()
t.right(90)
t.forward(100)
t.circle(100)
t.down()
wc.onclick(fxn)
turtle.done()
