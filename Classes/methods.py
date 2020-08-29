class Point:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter
    @classmethod
    def extra(cls):
        return cls(0, 1, "a")
    def draw(self):
        print(f"Point ({self.x}, {self.y}), {self.letter}")

# crate a function for this object

point1 = Point.extra()
point1.draw()

