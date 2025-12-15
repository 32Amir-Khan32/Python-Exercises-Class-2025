def calculate_grade(scores):
    average = sum(scores) / len(scores)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    return average, grade

def process_student(name, scores):
    avg, grade = calculate_grade(scores)
    print(f"\nStudent: {name}")
    print(f"Scores: {scores}")
    print(f"Average: {avg:.1f}")
    print(f"Grade: {grade}")
    
    if grade in ["A", "B"]:
        print("Status: Pass with honors")
    elif grade in ["C", "D"]:
        print("Status: Pass")
    else:
        print("Status: Fail")
    
    return avg, grade

# Process multiple students
students = {
    "AmirKhan": [85, 90, 88, 92],
    "Sara": [95, 98, 96, 94],
    "Ali": [70, 65, 75, 72],
    "Fatima": [55, 60, 58, 62]
}

for student_name, student_scores in students.items():
    process_student(student_name, student_scores)