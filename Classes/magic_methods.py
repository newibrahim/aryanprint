class Magic:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} and {self.y} is a string"
    def foo(self):
        print("This is string test")

magic1= Magic(1,4)
magic1.foo()
