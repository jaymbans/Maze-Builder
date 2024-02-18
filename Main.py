from Graphics import Window, Cell, Line, Point
from Maze import Maze

def main():
  win = Window(600,600)

  # cell_one = Cell(win)
  # #x1, y1, x2, y2
  # cell_one.draw(5, 5, 50, 50)
  # cell_two = Cell(win)
  # cell_two.draw(50,5,100,50)

  # cell_one.draw_move(cell_two, True)
  maze = Maze(10,10,6,6,50,50, win)
  
  win.wait_for_close()


main()