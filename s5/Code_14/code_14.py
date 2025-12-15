university_name = "Tech University"

def display_student(student_name):
    print(f"{student_name} studies at {university_name}")

display_student("AmirKhan")
display_student("Sara")

# Modifying global variable
def change_university(new_name):
    global university_name
    university_name = new_name

change_university("Science University")
display_student("Ali")