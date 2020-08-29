class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        
            print(self.x, self.y)

point1 = Point(1, 10)
point1.draw()