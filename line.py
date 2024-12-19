from tkinter import Canvas

class Line():

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, colour):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill = colour, width = 2)

    def __eq__(self, line):
        return self.point1 == line.point1 and self.point2 == line.point2
