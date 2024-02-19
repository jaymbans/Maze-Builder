from Graphics import Window, Point, Line, Cell
import time
import random

class Maze:
  def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
      self.x1 = x1
      self.y1 = y1
      self._num_rows = num_rows
      self._num_cols = num_cols
      self.cell_size_x = cell_size_x
      self.cell_size_y = cell_size_y
      self.win = win
      self._cells = []
      self._create_cells()
      self.seed = seed
      random.seed(self.seed)
      
  def _create_cells(self):
    # add rows
    for i in range(self._num_rows):
      # add cols
      row = []
      for j in range(self._num_cols):
        row.append(Cell(self.win))
      self._cells.append(row)
      for j in range(len(row)):
        self._draw_cell(i,j)
        self._animate()
    self._break_walls_r(0,0)

    # break entrance and exist
    self._break_entrance_and_exit()


  def _draw_cell(self, i, j):
    cell = self._cells[i][j]
    
    # calc offset
    cell.draw(
      j*self.cell_size_x+self.x1,
      i*self.cell_size_y+self.x1,
      j*self.cell_size_x+self.cell_size_x+self.x1,
      i*self.cell_size_y+self.cell_size_y+self.y1
    )

  def _animate(self):
    if(self.win):
      time.sleep(.1)
      self.win.redraw()

  def _break_entrance_and_exit(self):
    self._cells[0][0].has_top_wall = False
    self._draw_cell(0, 0)
    self._cells[self._num_rows - 1][self._num_cols - 1].has_bottom_wall = False
    self._draw_cell(self._num_rows - 1, self._num_cols - 1)
    self._reset_cells_visited()

  def _break_walls_r(self, i, j):
    self._cells[i][j].visited = True
    while True:
        next_index_list = []
        #left right up down
        # left
        if j > 0 and not self._cells[i][j - 1].visited:
            next_index_list.append((i, j - 1))
        # right
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
            next_index_list.append((i, j + 1))
        # up
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
            next_index_list.append((i + 1, j))
        # down
        if i > 0 and not self._cells[i - 1][j].visited:
            next_index_list.append((i - 1, j))

        # if there is nowhere to go from here
        # just break out
        if len(next_index_list) == 0:
            self._draw_cell(i, j)
            return

        # randomly choose the next direction to go
        direction_index = random.randrange(len(next_index_list))
        next_index = next_index_list[direction_index]

        # knock out walls between this cell and the next cell(s)
        # right
        if next_index[1] == j + 1:
            self._cells[i][j].has_right_wall = False
            self._cells[i][j + 1].has_left_wall = False
        # left
        if next_index[1] == j - 1:
            self._cells[i][j].has_left_wall = False
            self._cells[i][j - 1].has_right_wall = False
        # up
        if next_index[0] == i - 1:
            self._cells[i][j].has_top_wall = False
            self._cells[i - 1][j].has_bottom_wall = False
        # down
        if next_index[0] == i + 1:
            self._cells[i][j].has_bottom_wall = False
            self._cells[i + 1][j].has_top_wall = False

        # recursively visit the next cell
        self._break_walls_r(next_index[0], next_index[1])
    self._reset_cells_visited()

  def _reset_cells_visited(self):
    for r in self._cells:
      for c in r:
        c.visited = False
  
  def solve(self):
    return self._solve_r(0,0)
        
  def _solve_r(self, i,j):
    self._animate()
    cell = self._cells[i][j]
    cell.visited = True
    
    if(i==self._num_rows-1 and j==self._num_cols-1):
      return True
    
    # right
    if(j+1!=self._num_cols and
      not self._cells[i][j+1].visited and
        not cell.has_right_wall):
        cell.draw_move(self._cells[i][j+1])
        if(self._solve_r(i,j+1)):
          
          return True
        cell.draw_move(self._cells[i][j+1], True)

    # left
    if(j-1>=0 and
      not self._cells[i][j-1].visited and
        not cell.has_left_wall):
        cell.draw_move(self._cells[i][j-1])
        if(self._solve_r(i,j-1)):
          
          return True
        cell.draw_move(self._cells[i][j-1], True)
 
    # top
    if(i-1>=0 and
      not self._cells[i-1][j].visited and
        not cell.has_top_wall):
        cell.draw_move(self._cells[i-1][j])
        if(self._solve_r(i-1,j)):
          
          return True
        cell.draw_move(self._cells[i-1][j], True)

    # bottom
    if(i+1>=0 and
      not self._cells[i+1][j].visited and
        not cell.has_bottom_wall):
        cell.draw_move(self._cells[i+1][j])
        if(self._solve_r(i+1,j)):
          
          return True
        cell.draw_move(self._cells[i+1][j], True)

    return False