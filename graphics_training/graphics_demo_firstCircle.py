from graphics import *
import time

def main():
    win = GraphWin("My Window",500,500)
    win.setBackground('black')

    radius = 50

    pt = Point(250,250)
    cir =  Circle(pt, radius)
    cir.setFill('blue')
    cir.draw(win)

    time.sleep(10)

    for x in range(0,10):
        cir.move(5,0)
        time.sleep(0.01)

    win.getMouse()
    win.close()


main()
