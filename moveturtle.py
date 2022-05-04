from turtle import Turtle, Screen

TURTLE_SIZE = 20

screen = Screen()

yertle = Turtle(shape="turtle", visible=False)
#yertle.penup()
yertle.goto(TURTLE_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - TURTLE_SIZE/2)
yertle.pendown()
yertle.showturtle()

screen.mainloop()