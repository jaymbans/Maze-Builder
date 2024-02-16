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
  def __init__(self):
    self.x = 0
    self.y = 0

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

win = Window(800,600)

first_point = Point()

second_point = Point()
second_point.x = 50
second_point.y = 50

red_line = Line(first_point, second_point)
win.draw_line(red_line, "red")

win.wait_for_close()