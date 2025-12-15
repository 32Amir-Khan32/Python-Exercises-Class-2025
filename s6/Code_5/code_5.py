class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur
    
    def feed_milk(self):
        print(f"{self.name} is feeding milk to young")

class Dog(Mammal):
    def __init__(self, name, breed):
        super().__init__(name, has_fur=True)
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof woof!")
    
    def fetch(self):
        print(f"{self.name} is fetching the ball")

class Cat(Mammal):
    def __init__(self, name, color):
        super().__init__(name, has_fur=True)
        self.color = color
    
    def meow(self):
        print(f"{self.name} says: Meow!")
    
    def climb(self):
        print(f"{self.name} is climbing a tree")

# Create animals
dog = Dog("Rex", "German Shepherd")
cat = Cat("Whiskers", "Orange")

dog.eat()
dog.bark()
dog.fetch()
dog.feed_milk()

print()

cat.sleep()
cat.meow()
cat.climb()
print(f"{cat.name} has fur: {cat.has_fur}")