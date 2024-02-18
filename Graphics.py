from tkinter import Tk, BOTH, Canvas

# Window Class
class Window:

  def __init__(self, width, height):
    # static member variables
    self.width = width
    self.height = height

    # Tkinter class variables
    self.root = Tk()
    self.root.title("Maze Game")
    self.canvas = Canvas(self.root, width=self.width, height=self.height)
    self.is_running = False

    # Start Tkinter window
    self.canvas.pack()
    self.root.protocol("WM_DELETE_WINDOW", self.close)
    
  def close(self):
    self.is_running = False

  def redraw(self):
    self.root.update()
    self.root.update_idletasks()

  def wait_for_close(self):
    self.is_running = True
    while(self.is_running):
      self.redraw()

  def draw_line(self, line, color):
    line.draw(self.canvas, color)


# Point Class
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Line Class
class Line:
  def __init__(self, point_a, point_b):
    self.point_a = point_a
    self.point_b = point_b

  def draw(self, canvas, color):
    canvas.create_line(
      self.point_a.x,
      self.point_a.y,
      self.point_b.x,
      self.point_b.y,
      fill=color,
      width=2
    )
    canvas.pack()

# Cell Class
class Cell:
  def __init__(self, window):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._x1 = None
    self._x2 = None
    self._y1 = None
    self._y2 = None
    self._win = window
    self.color = "black"


  def draw(self, x1, y1, x2, y2):
    # set initials
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2
    
    # set top wall
    if(self.has_top_wall):
      top_wall = Line(Point(x1, y1),Point(x2,y1))
      top_wall.draw(self._win.canvas, "black")

    # set left wall
    if(self.has_left_wall):
      left_wall = Line(Point(x1, y1),Point(x1,y2))
      left_wall.draw(self._win.canvas, "black")

    # set right wall
    if(self.has_right_wall):
      right_wall = Line(Point(x2, y1),Point(x2,y2))
      right_wall.draw(self._win.canvas, "black")

    # set bottom wall
    if(self.has_bottom_wall):
      bottom_wall = Line(Point(x1, y2),Point(x2,y2))
      bottom_wall.draw(self._win.canvas, "black")