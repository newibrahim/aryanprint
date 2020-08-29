# using init function
class Book:
    def __init__(self, eye_color, height, weight):
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
    def Book(self):
        print("book")
    def read(self):
        print(f"You have {self.eye_color} eyes, your height is {self.height},and you weigh {self.weight} pounds")

book1 = Book("brown", "5 feet and 7 inches", 160)
book1.read()




