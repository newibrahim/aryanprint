class Book:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def book(self):
        pass
    def read(self):
        print(f"Read for {self.x}{self.y}{self.z}")
# Your book function should have a pass function

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def cord(self):
        print(f"({self.x}, {self.y}")
# Check if book1 is a object of the class Point

point1 = Point(1, 2)
book1 = Book(2, 7, 5)
print(isinstance(book1, Point))
