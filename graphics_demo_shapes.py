from graphics import *

def drawLine(x1,y1,x2,y2):
    return Line(Point(x1,y1), Point(x2,y2))

def drawRectangle(x1,y1,x2,y2):
    return Rectangle(Point(x1,y1), Point(x2,y2))

def drawCircle(x,y,r):
    return Circle(Point(x,y),r)


def main():
    win = GraphWin("My Window",500,500)
    win.setBackground('black')

    line = drawLine(250,250,250,350)
    line.setOutline(color_rgb(0,255,255))
    line.draw(win)

    rect = drawRectangle(100,100,200,200)
    rect.setOutline(color_rgb(255,0,255))
    rect.draw(win)

    cir = drawCircle(300,300,50)
    cir.setFill(color_rgb(255,255,0))
    cir.draw(win)


    win.getMouse()
    win.close()


main()
