student = {
    "name": "AmirKhan",
    "age": 25,
    "major": "CS",
    "city": "Tehran"
}

student.pop("city")
print(f"بعد از pop: {student}")

student.popitem()
print(f"بعد از popitem: {student}")

del student["age"]
print(f"بعد از del: {student}")

student.clear()
print(f"بعد از clear: {student}")