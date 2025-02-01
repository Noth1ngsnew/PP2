class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self,length):
        self.length = length
        
    def area(self):
        return self.length**2
    
shape=Shape()
print("Площадь Shape:", shape.area())

k=int(input("print lenth:"))
square = Square(k)
print("Площадь Square:", square.area())