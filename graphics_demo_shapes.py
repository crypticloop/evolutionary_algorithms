from graphics import *

def drawLine(x1,y1,x2,y2):
    return Line(Point(x1,y1), Point(x2,y2))

def main():
    win = GraphWin("My Window",500,500)
    win.setBackground('black')

    line = drawLine(250,250,250,350)
    line.setOutline(color_rgb(0,255,255))
    line.draw(win)

    



    win.getMouse()
    win.close()


main()
