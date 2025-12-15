class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def display_info(self):
        print(f"Shape: {self.name}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

# Create shapes
shapes = [
    Rectangle(5, 3),
    Circle(4),
    Triangle(6, 4, 6, 5, 5)
]

print("Shape Information:")
print("-" * 30)
for shape in shapes:
    shape.display_info()
    print()