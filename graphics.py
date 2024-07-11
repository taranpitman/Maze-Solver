from tkinter import Tk, BOTH, Canvas
import time

class Window():
    def __init__(self, width, height):
        self.__root = Tk() #assign a TKinter to self.root for later access and for defining title.
        self.__root.title("Maze Solver")
        self.w = Canvas(self.__root, width = width, height=height) #defines the canvas and assigns it to w, so this is what visually appears.
        self.w.pack(fill=BOTH, expand=1) #pack up the information so it can be created
        self.__running = False #used to check if the drawing functions are currently running, set to false by default.
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        #idk what these do exactly, but i think its just calls to manually redraw the sections as TKinter doesn't dynamically update

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed")
        #simple, if the programming is running, keep calling redraw

    def close(self):
        self.__running = False
        #just sets running to False, called when the window is closed by self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(self, line, fill_colour):
        line.draw(self.w, fill_colour)


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    def draw(self, canv, fill_colour="black"):
        canv.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_colour, width=2)
        #need to work out how to define coordinates for the above line?
        #print(canv, fill_colour)


        
