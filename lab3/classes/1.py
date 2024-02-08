class String:
    
    def getString(self):
        self.str = input()
    
    def printString (self):
        print(self.str.upper())

str = String()
str.getString()
str.printString()