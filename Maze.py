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


# Point Class
class Point:
  def __init__(self):
    self.x = 0
    self.y = 0



win = Window(800,600)
win.wait_for_close()