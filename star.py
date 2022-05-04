import turtle
star = turtle.Pen()
color=['red','blue','green','white'] 
turtle.bgcolor('black')
star.goto(-200,100)
star.width(4)
star.pencolor('pink')
star.forward(300)
 
for i in range(4):
    star.pencolor(color[i])
    star.width(4)
    star.right(144)
    star.forward(300)
     
turtle.done()