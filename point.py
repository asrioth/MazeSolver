class Point():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __eq__(self, point):
        if type(self) != type(point):
            return False
        return self.x == point.x and self.y == point.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"