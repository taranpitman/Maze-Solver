from cell import Cell
from graphics import Point, Line
import time, random
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y,win, seed=None):
        self.x1, self.y1, self.num_rows, self.num_cols, self.cell_size_x, self.cell_size_y, self._win, self.seed = x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win, seed
        #so x1/y1 are starting corner of the maze, num_rows is width, num_cols is height, cell_size is size of each cell.
        self._create_cells()
        if self.seed != None:
            print(f"seed set: f{seed}")
            random.seed(seed)
    def __repr__(self):
        return str(self)
    
    def _create_cells(self):
        self._cells = []
        x = self.x1
        for I in range(self.num_rows):
            temp = []
            y = self.y1
            for J in range(self.num_cols):
                c = Cell(x, x+self.cell_size_x, y, y+self.cell_size_y, self._win)
                temp.append(c)
                y += self.cell_size_y
            x += self.cell_size_x
            self._cells.append(temp)
        print("Cell list initialized.")
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self._draw_cell(i,j)
        print("Maze base drawn")
        #so it needs to create cells for each entry, list of lists
        #I = row, J = col, row is the main list, J is the inner list, so self.__cells[i][j]
        #track the current row and col, if row equals col, inc col then set row to 0

    def _draw_cell(self, I, J):
        x = self.x1 + (I * self.cell_size_x)
        y = self.y1 + (J * self.cell_size_y)
        #print(f"top left coord is: {x},{y}")
        self._cells[I][J].draw(Point(x,y), Point(x+self.cell_size_x,y+self.cell_size_y))
        self._animate()
    #This method should calculate the x/y position of the Cell based on i, j, the cell_size, and the x/y position of the Maze itself. 
    #The x/y position of the maze represents how many pixels from the top and left the maze should start from the side of the window.

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self._draw_cell(self.num_rows-1,self.num_cols-1)
        print("Entrance and exit made")
        #The entrance to the maze will always be at the top of the top-left cell, the exit always at the bottom of the bottom-right cell.
        #Add a _break_entrance_and_exit() method that removes an outer wall from those cells, and calls _draw_cell() after each removal.
    
    def _break_walls_R(self, I, J):
        #I = row, J = col
        self._cells[I][J].visited = True
        i = 0
        while i != 1:
            neighbours = []
            if J != 0:
                if self._cells[I][J-1].visited == False:
                    neighbours.append("t")
            if J != self.num_cols-1:
                if self._cells[I][J+1].visited == False:
                    neighbours.append("b")
            if I != 0:
                if self._cells[I-1][J].visited == False:
                    neighbours.append("l")
            if I != self.num_rows-1:
                if self._cells[I+1][J].visited == False:
                    neighbours.append("r")
            if len(neighbours) != 0:
                selected = neighbours[random.randrange(0,len(neighbours))]
            else:
                return
            match selected:
                case "t":
                    #print(f"current cell:{I,J}, next cell: {I, J-1}, selected = {selected}")
                    self._cells[I][J].has_top_wall = False
                    self._cells[I][J-1].has_bottom_wall = False
                    self._draw_cell(I,J)
                    self._draw_cell(I,J-1)
                    self._break_walls_R(I,J-1)
                case "b":
                    #print(f"current cell:{I,J}, next cell: {I, J+1}, selected = {selected}")
                    self._cells[I][J].has_bottom_wall = False
                    self._cells[I][J+1].has_top_wall = False
                    self._draw_cell(I,J)
                    self._draw_cell(I,J+1)
                    self._break_walls_R(I,J+1)
                case "l":
                    #print(f"current cell:{I,J}, next cell: {I-1, J},  selected = {selected}")
                    self._cells[I][J].has_left_wall = False
                    self._cells[I-1][J].has_right_wall = False
                    self._draw_cell(I,J)
                    self._draw_cell(I-1,J)
                    self._break_walls_R(I-1,J)
                case "r":
                    #print(f"current cell:{I,J}, next cell: {I+1, J},  selected = {selected}")
                    self._cells[I][J].has_right_wall = False
                    self._cells[I+1][J].has_left_wall = False
                    self._draw_cell(I,J)
                    self._draw_cell(I+1,J)
                    self._break_walls_R(I+1,J)

    def _reset_cells_visited(self):
        #I = row, J = col
        I, J = 0, 0
        while I < self.num_rows:
            while J < self.num_cols:
                self._cells[I][J].visited = False
                J += 1
            J = 0
            I += 1
            
    def solve(self):
        print("Solving the maze")
        return self._solve_R(I=0,J=0)
        

    def _solve_R(self,I,J):
        self._animate()
        self._cells[I][J].visited = True
        i = 0
        while i != 1:
            if I == self.num_rows-1 and J == self.num_cols-1:
                return True
            neighbours = []
            if J != 0:
                if self._cells[I][J-1].has_bottom_wall == False and self._cells[I][J-1].visited == False:
                    neighbours.append("t")
            if J != self.num_cols-1:
                if self._cells[I][J+1].has_top_wall == False and self._cells[I][J+1].visited == False:
                    neighbours.append("b")
            if I != 0:
                if self._cells[I-1][J].has_right_wall == False and self._cells[I-1][J].visited == False:
                    neighbours.append("l")
            if I != self.num_rows-1:
                if self._cells[I+1][J].has_left_wall == False and self._cells[I+1][J].visited == False:
                    neighbours.append("r")
            if len(neighbours) != 0:
                print(f"valid directions: {neighbours}")
                selected = neighbours[random.randrange(0,len(neighbours))]
                print(f"selected neighbour: {selected}")
            else:
                return False
            match selected:
                 #I = row, J = col
                case "t":
                    print(f"drawing line from cell at x:{self._cells[I][J].x1}, y:{self._cells[I][J].y1}")
                    print(f"drawing line from cell at x:{self._cells[I][J].x1}, y:{self._cells[I][J].y1}")
                    self._cells[I][J].draw_move(self._cells[I][J-1])
                    Answer = self._solve_R(I,J-1)
                    if Answer == False:
                        self._cells[I][J].draw_move(self._cells[I][J-1], True)
                case "b":
                    self._cells[I][J].draw_move(self._cells[I][J+1])
                    Answer = self._solve_R(I,J+1)
                    if Answer == False:
                        self._cells[I][J].draw_move(self._cells[I][J+1], True)
                case "l":
                    self._cells[I][J].draw_move(self._cells[I-1][J])
                    Answer = self._solve_R(I-1,J)
                    if Answer == False:
                        self._cells[I][J].draw_move(self._cells[I-1][J], True)
                case "r":
                    self._cells[I][J].draw_move(self._cells[I+1][J])
                    Answer = self._solve_R(I+1,J)
                    if Answer == False:
                        self._cells[I][J].draw_move(self._cells[I+1][J], True)
            if Answer == True:
                return True
                        
    


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        #time.sleep(0.05)
        #makes the maze load slower so you can appreciate the visuals of it, comment out the sleep to make it instant basically.