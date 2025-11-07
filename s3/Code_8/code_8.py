student = {
    "name": "AmirKhan",
    "age": 25,
    "major": "Computer Science"
}

print("کلیدها:")
for key in student:
    print(key)

print("\nمقادیر:")
for value in student.values():
    print(value)

print("\nکلید و مقدار:")
for key, value in student.items():
    print(f"{key}: {value}")