class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, my name is {self.name}")
    
    def celebrate_birthday(self):
        self.age += 1
        print(f"Happy birthday! Now I'm {self.age} years old")

# Create object
student = Person("AmirKhan")
student.age = 25
student.greet()
student.celebrate_birthday()