class Volume:
    def __init__(self, l, w, h):
        self.b = l * w
        self.h = h

    def rect(self):
        print(f"The volume of the rectangular prism is {self.b * self.h}")

    def trian(self):
        print(f"The volume of the triangular prism is {0.5 * self.b * self.h}")

    def pyra(self):
        print(f"The aproximate volume of the pyramid is {0.33 * self.b * self.h}")


rect = Volume(5, 6, 2)
tri = Volume(4, 12, 18)
pyra1 = Volume(10, 4, 60)
rect.rect()
tri.trian()
pyra1.pyra()
