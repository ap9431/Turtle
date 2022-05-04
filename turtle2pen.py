import turtle
colors=['red','purple','blue','green','orange','yellow']
t=turtle.Pen()
p=turtle.Pen()
turtle.bgcolor('black')
p.forward(50)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.right(90)

    p.pencolor(colors[x%6])
    p.width(x/100+1)
    p.forward(x)
    p.left(90)
  