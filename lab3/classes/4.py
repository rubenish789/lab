import math
class Point():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show (self):
        print ("The coordinates of the point is (", self.x, ",", self.y, ")\n")
    
    def move (self):
        x_old = self.x
        self.x = self.y
        self.y = x_old
        
    def dist (self, x2, y2):
        print ("The distance between two points is", math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2), "\n")
        
A = Point(int(input("x: ")), int(input("y: ")))

print("Before move: ")
A.show()

print("After move: ")
A.move()
A.show()

A.dist(int(input("The x of second point: ")), int(input("The y of second point: ")))