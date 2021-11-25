# class Calculadora():
#     def __init__(self, n1, n2):
#         self.suma = n1 + n2
#         self.resta = n1 - n2
#         self.producto= n1 * n2
#         self.division = n1 / n2

# def main():
#     operacion = Calculadora(1, 2)
#     print(operacion.producto)

# if __name__ == '__main__':
#     main()

import turtle
import math

class Drawing():
    def __init__(self, x, y, radius, color, outline, edgeWidth):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.outline = outline
        self.edgeWidth = edgeWidth

    def circle(self, turtle):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.width(self.edgeWidth)
        turtle.color(self.outline)
        turtle.fillcolor(self.color)
        turtle.setheading(0)
        turtle.speed('fastest')
        turtle.forward(self.radius)
        if self.color != 'transparent':
            turtle.begin_fill()
        turtle.pendown()
        points = 100
        for k in range(points):
            radians = (2*math.pi)*(k/points)
            turtle.goto(math.cos(radians)*self.radius + self.x, math.sin(radians)*self.radius + self.y)
        if self.color != 'transparent':
            turtle.end_fill()
        turtle.penup()
        turtle.goto(self.x, self.y)

    def rectangle(self, turtle):
        turtle.penup()
        turtle.color(self.color)
        if self.color != 'transparent':
            turtle.begin_fill()
        turtle.goto(self.x, self.y)
        turtle.width(self.edgeWidth)
        turtle.color(self.outline)
        turtle.fillcolor(self.color)
        turtle.setheading(0)
        turtle.speed('fastest')
        turtle.pendown()
        for i in range(0, 4):
            turtle.forward(self.radius)
            turtle.left(90)
        if self.color != 'transparent':
            turtle.end_fill()
        turtle.penup()
        turtle.goto(self.x, self.y)

    def setEdgeWidth(self, width):
        self.edgeWidth = width

    def setFill(self, color):
        self.color = color 
    
    def setOutline(self, outline):
        self.outline = outline

    def getX(self):
        return self.x

    def getY(self):
        return self.y 

    def getRadius(self):
        return self.redius 

def main():
    box = Drawing(x=-40, y=-40, radius=60, color='blue', outline='gold', edgeWidth=3)
    t = turtle.Turtle()
    screen = t.getscreen()
    box.rectangle(t)
    screen.exitonclick()

if __name__ == '__main__':
    main()
