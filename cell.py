from graphics import Line, Point
class Cell():
    def __init__(self, x1, x2, y1, y2, win, l_wall = True, r_wall = True, t_wall = True, b_wall = True, visited = False):
        self.x1, self.x2, self.y1, self.y2, self._win, self.has_left_wall, self.has_right_wall, self.has_bottom_wall, self.has_top_wall, self.visited = x1, x2, y1, y2, win, l_wall, r_wall, b_wall, t_wall, visited 
        #so define the cell with all the correct information

    def draw(self, a, b, fill_colour="black"):
        #so you give it the top left and bottom right of each cell (as points)and create new points using its info for each wall if the wall is to be drawn.
        if self.has_left_wall == True:
            e = Line(Point(a.x, a.y),Point(a.x, b.y))
            self._win.draw_line(e, fill_colour)
        else:
            e = Line(Point(a.x, a.y),Point(a.x, b.y))
            self._win.draw_line(e, "#d9d9d9")
        if self.has_top_wall == True:
            e = Line(Point(a.x, a.y),Point(b.x, a.y))
            self._win.draw_line(e, fill_colour)
        else:
            e = Line(Point(a.x, a.y),Point(b.x, a.y))
            self._win.draw_line(e, "#d9d9d9")
        if self.has_right_wall == True:
            e = Line(Point(b.x, a.y),Point(b.x, b.y))
            self._win.draw_line(e, fill_colour)
        else:
            e = Line(Point(b.x, a.y),Point(b.x, b.y))
            self._win.draw_line(e, "#d9d9d9")
        if self.has_bottom_wall == True:
            e = Line(Point(a.x, b.y),Point(b.x, b.y))
            self._win.draw_line(e, fill_colour)
        else:
            e = Line(Point(a.x, b.y),Point(b.x, b.y))
            self._win.draw_line(e, "#d9d9d9")
        #print("draws complete for cell")
    
    def draw_move(self, to_cell, undo=False):
        colour = "gray"
        if undo == False:
            colour = "red"
        #so if its not undo, its red, if its undo its grey
        start = Point(self.x1 + ((self.x2 - self.x1)/2), self.y1 + ((self.y2 - self.y1)/2))
        end = Point(to_cell.x1 + ((to_cell.x2 - to_cell.x1)/2), to_cell.y1 + ((to_cell.y2 - to_cell.y1)/2))
        #print(f"cell 1s coordinates are: {self.x1},{self.x2},{self.y1},{self.y2}")
        #print(f"cell 1s middle point is: x: {self.x1 + ((self.x2 - self.x1)/2)}, y: {self.y1 + ((self.y2 - self.y1)/2)}")
        #print(f"cell 2s coordinates are: {to_cell.x1},{to_cell.x2},{to_cell.y1},{to_cell.y2}")
        #print(f"cell 2s middle point is: x:{to_cell.x1 + ((to_cell.x2 - to_cell.x1)/2)}, y:{to_cell.y1 + ((to_cell.y2 - to_cell.y1)/2)}")

        #print(f"line drawn between{self.x1 + ((self.x2 - self.x1)/2)}, {self.y1 + ((self.y2 - self.y1)/2)} and {to_cell.x1 + ((to_cell.x2 - to_cell.x1)/2)}, {to_cell.y1 + ((to_cell.y2 - to_cell.y1)/2)}")
        path = Line(start,end)
        self._win.draw_line(path, colour)
        #get the middle point of the start cell and other cell, then draw a line between them.
        #NOT YET TESTED SORRY