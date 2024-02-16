from Graphics import Window, Line, Point

def main():
  win = Window(800,600)
  first_point = Point()

  second_point = Point()
  second_point.x = 50
  second_point.y = 50

  red_line = Line(first_point, second_point)
  win.draw_line(red_line, "red")

  win.wait_for_close()


main()