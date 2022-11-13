import math
import turtle

ecran = turtle.Screen()
turtle.speed(0)

def makeLine():
    base = turtle.pos()
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(600)
    turtle.setheading(90)
    turtle.forward(5)
    turtle.goto(base[0], base[1]+5)
    turtle.end_fill()

def makeColumn():
    base = turtle.pos()
    turtle.begin_fill()
    turtle.setheading(90)
    turtle.forward(480)
    turtle.setheading(0)
    turtle.forward(5)
    turtle.goto(base[0]+5, base[1])
    turtle.end_fill()

def Piece(line, colum, player):
    color = "blue"
    if player == 1:
        color = "red"
    turtle.color(color)
    origin = (-300, -250)
    turtle.penup()
    turtle.goto(-258+colum*86, -239+line*80)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

def posToRC(x,y):
    print(math.floor((x + 300)/85), math.floor((y+250)/80))
    return math.floor((x + 300)/85)

turtle.penup()
turtle.goto(-300, -250)
turtle.pendown()
makeColumn()

for f in range(7):
    turtle.penup()
    turtle.goto(-300,-250+f*80)
    turtle.pendown()
    makeLine()
    turtle.penup()
    turtle.goto(-300+(f+1)*85, -250)
    turtle.pendown()
    makeColumn()

turtle.setheading(0)

ecran.onclick(posToRC)
turtle.mainloop()