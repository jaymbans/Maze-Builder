from Graphics import Window, Point, Line, Cell
import time

class Maze:
  def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
      self.x1 = x1
      self.y1 = y1
      self.num_rows = num_rows
      self.num_cols = num_cols
      self.cell_size_x = cell_size_x
      self.cell_size_y = cell_size_y
      self.win = win
      self.cells = []
      self._create_cells()

  def _create_cells(self):
    # add rows
    for i in range(self.num_rows):
      # add cols
      row = []
      for j in range(self.num_cols):
        row.append(Cell(self.win))
      self.cells.append(row)
      for j in range(len(row)):
        self._draw_cell(i,j)
        self._animate()


  def _draw_cell(self, i, j):
    cell = self.cells[i][j]
    
    # calc offset
    cell.draw(
      j*self.cell_size_x+self.x1,
      i*self.cell_size_y+self.x1,
      j*self.cell_size_x+self.cell_size_x+self.x1,
      i*self.cell_size_y+self.cell_size_y+self.y1
    )

  def _animate(self):
    time.sleep(.1)
    self.win.redraw()
    
        



