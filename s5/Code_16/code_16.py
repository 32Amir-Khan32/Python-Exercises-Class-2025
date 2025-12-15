def print_student_details(**student_info):
    print("Student Details:")
    for key, value in student_info.items():
        print(f"  {key.title()}: {value}")

print_student_details(name="AmirKhan", age=25, major="CS", university="Tech University")
print_student_details(name="Ali", gpa=3.7, year="Junior")