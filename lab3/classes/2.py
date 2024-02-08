class Shape:
    def area(self):
        print("Shape's area is 0")

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print("Sqaure's area is", self.length ** 2)

a = Shape()
b = Square(int(input()))

a.area()
b.area()