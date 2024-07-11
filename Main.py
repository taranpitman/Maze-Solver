from graphics import Window, Point, Line # type: ignore
from maze import Maze
from cell import Cell

    
def main():
    num_rows = 12
    num_cols = 12
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()
    maze._break_walls_R(0,0)
    print("Maze built")
    maze._reset_cells_visited()
    final = maze.solve()
    print(final)
    #anything you do should go before this, as wait_for_close() is essentially the ending
    win.wait_for_close()
main()

