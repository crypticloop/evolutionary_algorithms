from graphics import *

def main():
    win = GraphWin("My Window",500,500)
    #win.setBackground('black')

    # Text defaults to black, ensure does not clash with background
    # The center of the text anchors to the point
    txt = Text(Point(250, 250), "What's up?")
    txt.draw(win)

    win.getMouse()
    win.close()


main()
