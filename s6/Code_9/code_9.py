class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, a, b):
        self.result = a + b
        return self.result
    
    def multiply(self, a, b):
        self.result = a * b
        return self.result
    
    def get_last_result(self):
        return self.result

calc = Calculator()
print(f"Addition: 5 + 3 = {calc.add(5, 3)}")
print(f"Multiplication: 4 * 7 = {calc.multiply(4, 7)}")
print(f"Last result: {calc.get_last_result()}")