#OOP - Modules
# import turtle

# t = turtle.Turtle()
# screen = t.getscreen()
# t.forward(25)
# t.left(90)
# t.forward(25)
# t.left(90)
# t.forward(25)
# t.left(90)
# t.forward (25)
# screen.exitonclick()

# from turtle import *
#TO ASSIGN COLORS. IF 255 COLORS SCALE IS USED, 
#BECOMES NECESSARY TO DEFINE COLORMODE(255) BEFORE. 
#REMIND TO ASSIGN THIS COLOR "TUPPLE" METHOD TO OBJECT "t" AS WELL.
# t=Turtle()
# screen=t.getscreen()
# pencolor_c=screen.textinput("Let's draw!", "Please enter the pencolor: ")
# fillcolor_c=screen.textinput("Let's draw!", "Please enter the fillcolor: ")
# t.color(pencolor_c, fillcolor_c)
# t.begin_fill()
# t.circle(50)
# t.end_fill()
# print(t.color())
# screen.exitonclick()

# DRAWING DOTS
# from turtle import *
# t=Turtle()
# screen=t.getscreen()
# t.fd(50)
# t.dot(10, "red")
# t.left(90)
# t.fd(50)
# screen.exitonclick()

# from turtle import *

# t=Turtle()
# screen=t.getscreen()

# t.hideturtle()
# t.fd(150) #avanzar 150
# t.begin_fill() #amarillo carro
# t.fillcolor('yellow')
# t.fd(100)
# t.left(90)
# t.fd(100)
# t.left(90)
# t.fd(100)
# t.right(45)
# t.fd(100)
# t.left(45)
# t.fd(100)
# t.left(90)
# t.fd(50*((2)**(1/2)))
# t.right(90)
# t.fd(230)
# t.left(90)
# t.fd(100)
# t.left(90)
# t.fd(100)
# t.end_fill()#acaba amarillo carro

# t.begin_fill()
# t.fillcolor('black')
# t.circle(-40)
# t.end_fill()

# t.fd(300)
# t.begin_fill()
# t.fillcolor('black')
# t.circle(-40)
# t.end_fill()

# screen.exitonclick()


# from turtle import *

# t=Turtle()
# t2=Turtle()
# screen=t.getscreen()
# t2.back(50)
# sides=int(textinput("Polygon", "Please enter the number of sides: "))
# for i in range(sides):
#     t.fd(200//sides)
#     t.left(360//sides)
# screen.exitonclick()

#READING XML FILES
# from xml.dom import minidom

# xmldoc = minidom.parse("hey.xml")
# graphicsCommand = xmldoc.getElementsByTagName('GraphicsCommands')[0]
# commands = graphicsCommand.getElementsByTagName('Command')
# commandList = []
# xList = []
# yList = []
# widthList = []
# colorList = []
# radiusList = []
# attributeList = [xList, yList, widthList, colorList, radiusList]
# attributes = ["x","y","width","color","radius"]
# for command in commands:
#     commandList.append(command.firstChild.data.strip())
#     attr = command.attributes
#     for i in range(len(attributes)):
#         attr = command.attributes
#         key = attributes[i]
#         if key in attr:
#             attributeList[i].append(attr[key].value)
#         else:
#             attributeList[i].append(None)

# from turtle import Turtle

# t=Turtle()
# screen=t.getscreen()
# screen.colormode(255)
# screen.tracer(0)
# for i in range(len(commandList)):
#     command=commandList[i]
#     if command=="PenUp":
#         t.penup()
#     elif command=="PenDown":
#         t.pendown()
#     elif command=="GoTo":
#         x=float(xList[i])
#         y=float(xList[i])
#         width=float(widthList[i])
#         color=colorList[i]
#         t.width(width)
#         t.color(color)
#         t.goto(x, y)
#     elif command=="Circle":
#         radius=float(radiusList[i])
#         width=float(widthList[i])
#         color=colorList[i]
#         t.width(width)
#         t.pencolor(color)
#         t.circle(radius)
#     elif command=="BeginFill":
#         color=colorList[i]
#         t.fillcolor(color)
#         t.begin_fill()
#     elif command=="EndFill":
#         t.end_fill()
#     else:
#         print("Unknown commands", command)
# screen.update()


#HOW 2 GRAPHIC GENERAL FUNCTIONS. 
from turtle import Turtle, Screen

WIDTH, HEIGHT = 40, 40  # coordinate system size

def plotter(turtle, x):
    turtle.penup()
    turtle.pencolor('blue')
    while x < 20:
        y = (x**4)/4 - (x**3)/3 - 3*x**2
        turtle.goto(x, y)
        turtle.pendown()
        x=x+0.1

def axis(turtle, distance, tick):
    position = turtle.position()
    turtle.pendown()

    for _ in range(0, distance // 2, tick):
        turtle.forward(tick)
        turtle.dot()

    turtle.setposition(position)

    for _ in range(0, distance // 2, tick):
        turtle.backward(tick)
        turtle.dot()

screen = Screen()
screen.setworldcoordinates(-WIDTH/2, -HEIGHT/2, WIDTH/2, HEIGHT/2)

ivy = Turtle(visible=False)
ivy.speed('fastest')
ivy.penup()
axis(ivy, WIDTH, 1)

ivy.penup()
ivy.home()
ivy.setheading(90)
axis(ivy, HEIGHT, 1)

plotter(ivy, -20)
screen.exitonclick()