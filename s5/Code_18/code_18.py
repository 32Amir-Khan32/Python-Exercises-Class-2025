def calculate_average(*scores):
    total = sum(scores)
    average = total / len(scores)
    return average

student_avg = calculate_average(85, 90, 88, 92, 87)
print(f"Student Average: {student_avg:.1f}")
print(f"Test 1 Average: {calculate_average(75, 80, 85):.1f}")