class Shape:
    
    def area(self):
        print("Shape's area is 0")
        
class Ractangle(Shape):
    
    def __init__ (self, length, wigth):
        self.length = length
        self.wigth = wigth
    
    def area(self):
        print ("Rectangle's area is", self.length * self.wigth)

a = Shape()
b = Ractangle(int(input()), int(input()))

a.area()
b.area()