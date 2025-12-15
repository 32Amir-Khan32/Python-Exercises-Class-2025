def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

print("Temperature Conversions:")
print(f"77°F = {fahrenheit_to_celsius(77):.1f}°C")
print(f"95°F = {fahrenheit_to_celsius(95):.1f}°C")
print(f"50°F = {fahrenheit_to_celsius(50):.1f}°C")