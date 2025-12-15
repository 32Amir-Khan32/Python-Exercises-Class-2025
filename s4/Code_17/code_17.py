students = [
    {"name": "AmirKhan", "age": 25, "grades": [85, 90, 88]},
    {"name": "Sara", "age": 23, "grades": [92, 95, 89]},
    {"name": "Ali", "age": 22, "grades": [78, 82, 75]},
    {"name": "Fatima", "age": 24, "grades": [88, 85, 90]}
]

print("Student Performance Report")
print("=" * 50)

for student in students:
    name = student["name"]
    age = student["age"]
    grades = student["grades"]
    
    # Calculate average
    average = sum(grades) / len(grades)
    
    # Determine grade
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    # Check if student passes
    if average >= 70:
        status = "PASS"
    else:
        status = "FAIL"
    
    # Display results
    print(f"Student: {name} (Age: {age})")
    print(f"Grades: {grades}")
    print(f"Average: {average:.1f}")
    print(f"Grade: {letter_grade}")
    print(f"Status: {status}")
    
    # Additional comments
    if letter_grade == "A":
        print("Comment: Excellent work!")
    elif letter_grade == "B":
        print("Comment: Good job!")
    elif letter_grade == "C":
        print("Comment: Needs improvement")
    
    print("-" * 50)