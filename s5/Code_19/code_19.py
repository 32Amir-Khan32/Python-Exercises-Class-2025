def create_full_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

student1 = create_full_name("Amir", "Khan")
student2 = create_full_name("Sara", "Johnson")

print(f"Student 1: {student1}")
print(f"Student 2: {student2}")