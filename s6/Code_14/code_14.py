class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # Protected attribute
    
    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            print("Temperature cannot be below absolute zero!")
            self._celsius = -273.15
        else:
            self._celsius = value
    
    @property
    def fahrenheit(self):
        """Read-only property for fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        """Read-only property for kelvin"""
        return self._celsius + 273.15
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Alternative constructor from fahrenheit"""
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
    def display(self):
        print(f"Celsius: {self.celsius:.1f}°C")
        print(f"Fahrenheit: {self.fahrenheit:.1f}°F")
        print(f"Kelvin: {self.kelvin:.1f}K")

# Create temperature objects
temp1 = Temperature(25)
temp2 = Temperature.from_fahrenheit(77)

print("Temperature 1:")
temp1.display()

print("\nTemperature 2 (from 77°F):")
temp2.display()

print("\nTesting setter with validation:")
temp1.celsius = -300  # Should be limited to -273.15
temp1.display()

temp1.celsius = 100  # Valid temperature
print("\nAfter setting to 100°C:")
temp1.display()