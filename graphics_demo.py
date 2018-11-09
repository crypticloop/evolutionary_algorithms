from graphics import *

def main():
    win = GraphWin("My Window",500,500)
    win.setBackground('black')

    pt = Point(250,250)
    cir =  Circle(pt, 50)
    cir.setFill('blue')
    cir.draw(win)

    win.getMouse()
    win.close()


main()
